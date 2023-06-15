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
    def read_parameter(region_name, parameter, decrypt=False):
        ssm_client = boto3.client("ssm", region_name=region_name)
        return ssm_client.get_parameter(Name=parameter, WithDecryption=decrypt)[
            "Parameter"
        ]["Value"]

    def _create_sql_engine(self, region_name, user_parameter, password_parameter, host):
        self.engine = create_engine(
            f"""redshift+psycopg2://{self.read_parameter(region_name, user_parameter, True)}:{quote(self.read_parameter(region_name, password_parameter, True))}@{host}"""
        )

    def download_data(self, sql):
        downloaded_data = pd.DataFrame()
        iteration = 0
        for chunk in pd.read_sql_query(text(sql), self.engine, chunksize=5000):
            downloaded_data = downloaded_data.append(chunk, ignore_index=True)

        return downloaded_data

    def execute_sql_query(self, sql):
        return self.engine.execute(sql)
