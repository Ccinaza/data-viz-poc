import pandas as pd
from clickhouse_driver import Client

# Load the CSV files
sales_df = pd.read_csv('/Users/blessingangus/Downloads/data_engineering/personal_de_projects/data-viz-poc/test_data/sales_data.csv')
user_df = pd.read_csv('/Users/blessingangus/Downloads/data_engineering/personal_de_projects/data-viz-poc/test_data/user_data.csv')
regional_df = pd.read_csv('/Users/blessingangus/Downloads/data_engineering/personal_de_projects/data-viz-poc/test_data/regional_data.csv')

# Convert date columns to datetime
sales_df['date'] = pd.to_datetime(sales_df['date']).dt.date
user_df['join_date'] = pd.to_datetime(user_df['join_date']).dt.date

# Connect to ClickHouse
client = Client(host='localhost', port=9000, user='default', password='password', database='default')

# Create database
client.execute('CREATE DATABASE IF NOT EXISTS analytics')
client.execute('USE analytics')

# Create tables
client.execute('''
CREATE TABLE IF NOT EXISTS sales_data (
    date Datetime,
    region String,
    category String,
    quantity Int32,
    unit_price Float64,
    discount Float64,
    final_price Float64,
    total_sale Float64
) ENGINE = MergeTree()
ORDER BY (date, region)
''')

client.execute('''
CREATE TABLE IF NOT EXISTS user_data (
    user_id Int32,
    username String,
    department String,
    access_level String,
    join_date Datetime
) ENGINE = MergeTree()
ORDER BY user_id
''')

client.execute('''
CREATE TABLE IF NOT EXISTS regional_data (
    region String,
    metric String,
    month Int32,
    value Float64,
    target Float64,
    year Int32
) ENGINE = MergeTree()
ORDER BY (region, metric, month)
''')

# Insert data
client.execute('TRUNCATE TABLE IF EXISTS sales_data')
client.execute('TRUNCATE TABLE IF EXISTS user_data')
client.execute('TRUNCATE TABLE IF EXISTS regional_data')

client.insert_dataframe('INSERT INTO sales_data VALUES', sales_df)
client.insert_dataframe('INSERT INTO user_data VALUES', user_df)
client.insert_dataframe('INSERT INTO regional_data VALUES', regional_df)

print("Data loaded into ClickHouse successfully!")
