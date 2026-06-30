# importing the libraries 
import pandas as pd
import logging
import os

# setting up logging configuration
logging.basicConfig(filename='logs/pipeline.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('ETL pipeline started.')

#ETL function to extract data from CSV file
df = pd.read_csv('data/raw_sales.csv')
logging.info(f"Extracted {len(df)} records.")