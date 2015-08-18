This sample code works with PostgreSQL database only

1. Install the required Python modules, see the [Required Software](https://github.com/htquach/ArPrData/wiki#required-software) section in the Wiki
2. Create an empty database (recommended) or use an existing database.
3. Run the [postgresql_sample_schema.sql](https://github.com/htquach/ArPrData/blob/master/samples/postgresql_sample_schema.sql) file to install the ArPrDataDemo database schema.
4. Set the environment variable `DB_URL_ENV_NAME` that contains the connection string
   `export DB_URL_ENV_NAME="postgresql://<username>:<password>@<db_host>:<db_port>/<dbname>"`
5. Review [samples/policies.yml](https://github.com/htquach/ArPrData/blob/master/samples/policies.yml)
6. Run `python main.py`
7. Verify the content of the ArPrDataDemo.Table1 and ArPrDataDemo.Table2 are consistent with the policy defined in [samples/policies.yml](https://github.com/htquach/ArPrData/blob/master/samples/policies.yml)
