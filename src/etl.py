# importing the libraries 
import json
import pandas as pd
import logging
import os


# loading configuration from config.json
with open("config.json", "r") as file:
    config = json.load(file)

INPUT_FILE = config["input_file"]
OUTPUT_FILE = config["output_file"]
LOG_FILE = config["log_file"]


# setting up logging configuration
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('ETL pipeline started.')

#ETL function to extract data from CSV file
df = pd.read_csv(INPUT_FILE)
logging.info(f"Extracted {len(df)} records.")

# Transforming the data
df = df.drop_duplicates() # removing duplicates
df = df.dropna() # removing missing values
df["Total"] = df["Quantity"] * df["Price"] # calculating total sales
df["Customer"] = df["Customer"].str.upper() # standardizing customer names
logging.info("Data transformation completed.")  

# Loading the data into a new CSV file
df.to_csv(OUTPUT_FILE, index=False)
logging.info("Data loaded into cleaned_sales.csv.")
print("ETL pipeline completed successfully.")
logging.info('ETL pipeline completed successfully.')