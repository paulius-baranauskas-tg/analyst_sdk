import boto3

from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *
from urllib.parse import quote
from datetime import datetime
import pandas as pd


def _read_parameter(parameter: str, decrypt: bool) -> str:
    """Internal function to read parameters from aws parameter store.
    Args:
        parameter (str): Parameter name
        decrypt (bool): Boolean to use encrypted or not value.
    Returns:
        str: Parameter value.
    """
    ssm_client = boto3.client("ssm")
    return ssm_client.get_parameter(Name=parameter, WithDecryption=decrypt)[
        "Parameter"
    ]["Value"]


def get_user() -> str:
    """Gets Redshift user name.
    Returns:
        str: User name for Redshift.
    """
    return _read_parameter(parameter="/DataTeam/Redshift/ml_user", decrypt=False)


def get_password() -> str:
    """Gets Redshift password.
    Returns:
        str: Redshift password.
    """
    return _read_parameter(
        parameter="/DataTeam/Redshift/ml_user_password", decrypt=True
    )


def execute_sql_query(sql, engine):
    """Executes SQL query remotely. No data downloading.
    Args:
        sql (str): SQL query.
        engine (str): Formatted engine string.
    Returns:
        _type_: Any response server sends.
    """
    return engine.execute(sql)


def create_sql_engine(host):
    """Prepares an sql engine string that can be used in download_data or execute_sql_query functions
    Args:
        host (str): Host address for sql.
    Returns:
        srt: string formatted for usage.
    """    
    return create_engine(
        f"""redshift+psycopg2://{get_user()}:{quote(get_password())}@{host}"""
    )


def download_data(sql, engine):
    """Runs SQL query and downloads data to Pandas DataFrame.
    Args:
        sql (str): SQL query that is used for downloading data.
        engine (str): Already created driver.
    Returns:
        pd.DataFrame: output dataframe.
    """

    downloaded_data = pd.DataFrame()
    iteration = 0
    for chunk in pd.read_sql_query(text(sql), engine, chunksize=5000):
        print(f"iteration {iteration}: {datetime.now()}")
        downloaded_data = downloaded_data.append(chunk, ignore_index=True)

    return downloaded_data