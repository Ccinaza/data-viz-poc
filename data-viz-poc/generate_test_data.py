import pandas as pd
import numpy as np
import os
import sqlalchemy
from sqlalchemy import create_engine
from datetime import datetime, timedelta

# Create output directory
os.makedirs('test_data', exist_ok=True)

# Generate sample sales data
def generate_sales_data(num_records=1000):
    # Create date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # Create regions and product categories
    regions = ['North', 'South', 'East', 'West', 'Central']
    categories = ['Electronics', 'Clothing', 'Home Goods', 'Groceries', 'Office Supplies']
    
    # Generate random data
    sales_data = []
    for _ in range(num_records):
        date = np.random.choice(dates)
        region = np.random.choice(regions)
        category = np.random.choice(categories)
        quantity = np.random.randint(1, 50)
        price = np.round(np.random.uniform(10, 500), 2)
        discount = np.round(np.random.uniform(0, 0.3), 2)
        final_price = np.round(price * (1 - discount), 2)
        total = np.round(quantity * final_price, 2)
        
        sales_data.append({
            'date': date,
            'region': region,
            'category': category,
            'quantity': quantity,
            'unit_price': price,
            'discount': discount,
            'final_price': final_price,
            'total_sale': total
        })
    
    return pd.DataFrame(sales_data)

# Generate user data for testing access controls
def generate_user_data(num_users=50):
    departments = ['Sales', 'Marketing', 'Finance', 'HR', 'IT', 'Operations']
    access_levels = ['Basic', 'Intermediate', 'Advanced', 'Admin']
    
    user_data = []
    for i in range(num_users):
        department = np.random.choice(departments)
        access_level = np.random.choice(access_levels)
        join_date = datetime.now() - timedelta(days=np.random.randint(1, 1000))
        
        user_data.append({
            'user_id': i + 1,
            'username': f'user_{i + 1}',
            'department': department,
            'access_level': access_level,
            'join_date': join_date
        })
    
    return pd.DataFrame(user_data)

# Generate regional performance data
def generate_regional_data():
    regions = ['North', 'South', 'East', 'West', 'Central']
    metrics = ['Revenue', 'Profit', 'Cost', 'Customer Acquisition', 'Retention']
    
    regional_data = []
    for region in regions:
        for metric in metrics:
            for month in range(1, 13):
                value = np.round(np.random.uniform(10000, 100000), 2)
                target = np.round(value * np.random.uniform(0.9, 1.2), 2)
                
                regional_data.append({
                    'region': region,
                    'metric': metric,
                    'month': month,
                    'value': value,
                    'target': target,
                    'year': 2024
                })
    
    return pd.DataFrame(regional_data)

# Generate the data
sales_df = generate_sales_data(5000)
user_df = generate_user_data(100)
regional_df = generate_regional_data()

# Save as CSV
sales_df.to_csv('test_data/sales_data.csv', index=False)
user_df.to_csv('test_data/user_data.csv', index=False)
regional_df.to_csv('test_data/regional_data.csv', index=False)

print("CSV files generated in test_data directory")

# Function to load data into PostgreSQL
def load_to_postgres(host, port, user, password, db, schema='public'):
    connection_string = f'postgresql://{user}:{password}@{host}:{port}/{db}'
    engine = create_engine(connection_string)
    
    # Load each dataset to the database
    sales_df.to_sql('sales_data', engine, schema=schema, if_exists='replace', index=False)
    user_df.to_sql('user_data', engine, schema=schema, if_exists='replace', index=False)
    regional_df.to_sql('regional_data', engine, schema=schema, if_exists='replace', index=False)
    
    print(f"Data loaded into PostgreSQL at {host}:{port}/{db}")

# Instructions for loading data
print("\nTo load data into PostgreSQL for each tool, run:")
print("For LightDash: python3 -c \"from generate_test_data import load_to_postgres; load_to_postgres('localhost', 5432, 'warehouse', 'password', 'warehouse')\"")
print("For Metabase: First connect to the sample database in the UI")
print("For Superset: First create a database connection in the UI, then import CSV files")