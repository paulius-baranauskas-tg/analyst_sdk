from setuptools import setup

setup(
    name='tgo_analyst_sdk',
    version='0.0.3',
    description='Commonly used custom Python functions in analytical tasks.',
    packages=['tgo_analyst_sdk'],
    author='Paulius Baranauskas',
    author_email='paulius.baranauskas@transfergo.com',
    url='https://github.com/pauliusbar/analyst_sdk',
    install_requires=["dateutil", "datetime", "sklearn", "matplotlib", "boto3", "sqlalchemy", "urllib", "pandas", "sqlalchemy-redshift", "redshift_connector", "psycopg2-binary"]
)