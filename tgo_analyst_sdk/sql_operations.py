import boto3

from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *
from urllib.parse import quote
from datetime import datetime
import pandas as pd


class sql_operations:
    def __init__(
        self, region_name, user_parameter_name, password_parameter_name, server_host
    ):
        self._create_sql_engine(
            region_name, user_parameter_name, password_parameter_name, server_host
        )

    @staticmethod
    def read_parameter(region_name: str, parameter: str, decrypt=False):
        """Reads parameter value from AWS Parameter Store.
        This is a wrapper to Boto3 get_parameter method.
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_parameter.html

        Args:
            region_name (str): AWS Region name.
            parameter (str): Parameter name in AWS Parameter Store.
            decrypt (bool, optional): Return decrypted values for secure string parameters. Defaults to False.

        Returns:
            str: Value of parameter selected from dictionary.
        """
        ssm_client = boto3.client("ssm", region_name=region_name)
        return ssm_client.get_parameter(Name=parameter, WithDecryption=decrypt)[
            "Parameter"
        ]["Value"]

    def _create_sql_engine(
        self, region_name: str, user_parameter: str, password_parameter: str, host: str
    ):
        """Creates Redshift SQL engine in SQLAlchemy.

        Args:
            region_name (str): AWS region name.
            user_parameter (str): User parameter name in AWS Parameter Store.
            password_parameter (str): Password parameter name in AWS Parameter Store.
            host (str): Redshift server host address.

        Returns:
            sqlalchemy.engine.base.Engine: Redshift SQL engine populated with region, username, password, host.
        """
        self.engine = create_engine(
            f"""redshift+psycopg2://{self.read_parameter(region_name, user_parameter, True)}:{quote(self.read_parameter(region_name, password_parameter, True))}@{host}"""
        )

    def download_data(self, sql: str):
        """Uses SQLAlchemy to download data and populate it to Pandas DataFrame.

        Args:
            sql (str): SQL query.

        Returns:
            pandas.core.frame.DataFrame: Pandas DataFrame with downloaded data.
        """
        downloaded_data = pd.DataFrame()
        for chunk in pd.read_sql_query(text(sql), self.engine, chunksize=5000):
            downloaded_data = downloaded_data.append(chunk, ignore_index=True)

        return downloaded_data

    def execute_sql_query(self, sql: str):
        """Uses SQLAlchemy execute method to execute sql query inside database.
        This method does not return any data.

        Args:
            sql (str): SQL query to execute in database.
        """
        self.engine.execute(sql)
