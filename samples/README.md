This sample code works with PostgreSQL database only

1. Install the required Python module, see the [Required Software](https://github.com/htquach/ArPrData/wiki#required-software) section in the Wiki
2. Create an empty data (recommended) or use an existing database.
3. Run the [postgresql_sample_schema.sql](https://github.com/htquach/ArPrData/blob/master/samples/postgresql_sample_schema.sql) file to install the ArPrDataDemo schema.
4. Create an environment variable that contains the connection string
   `export DB_URL_ENV_NAME="postgresql://<username>:<password>@<db_host>:<db_port>/<dbname>"`
5. Review [samples/policies.yml](https://github.com/htquach/ArPrData/blob/master/samples/policies.yml)
5. Run `python main.py`

