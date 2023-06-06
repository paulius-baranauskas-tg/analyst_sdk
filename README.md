# tgo_analyst_sdk

## Definition

Most common pyhton functions used in TransferGo analytical scripts.

## Installation

To install this package, use:

```bash
pip install git+https://github.com/paulius-baranauskas-tg/analyst_sdk@master
```

If pip or git is not available (for example, when using conda environments), you need to install git and pip. This can be done using this command:

```bash
conda install git pip
```

Requires: `dateutils`, `scikit-learn`, `boto3`, `sqlalchemy`, `pandas`, `sqlalchemy-redshift`, `redshift_connector`, `psycopg2-binary`. All installed during setup.

## Usage

This library has two main function groups: `date_operations` and `sql_operations`.

`date_operations` contains functions that make it easier to add periods in Python, generate range, convert types.

```Python
from tgo_analyst_sdk.date_operations import date_add, generate_date_range
```

`sql_operations` contains functions to get connection to Redshift server details, such as user name and password. It also contains wrappers for downloading data and executing sql queries.

```Python
from tgo_analyst_sdk.sql_operations import get_user, download_data
```
