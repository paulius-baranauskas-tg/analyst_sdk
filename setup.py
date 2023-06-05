from setuptools import setup

setup(
    name='tgo_analyst_sdk',
    version='0.0.3',
    description='Commonly used custom Python functions in analytical tasks.',
    packages=['tgo_analyst_sdk'],
    author='Paulius Baranauskas',
    author_email='paulius.baranauskas@transfergo.com',
    url='https://github.com/pauliusbar/analyst_sdk',
    install_requires=[
        "dateutils>=0.6.12",
        "sklearn>=1.0",
        "boto3>=1.26",
        "sqlalchemy>=2.0",
        "urllib>=2.0",
        "pandas>=1.5",
        "sqlalchemy-redshift>=0.8.14",
        "redshift_connector>=2.0.910",
        "psycopg2-binary>=2.9.6"]
)