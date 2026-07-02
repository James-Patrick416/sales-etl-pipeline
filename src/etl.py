# importing the libraries 
import json
import pandas as pd
import logging
import os
import sqlite3
from analytics import run_analytics
from report import generate_report
from charts import generate_chart

# loading configuration from config.json
def load_config():
    with open("config.json", "r") as file:
        return json.load(file)


# loading to SQLite database
def load_to_database(df, database_file):
    logging.info("Loading data into SQLite database...")

    # Connect to the database (creates it if it doesn't exist)
    connection = sqlite3.connect(database_file)

    # Write the DataFrame to a table named 'sales'
    df.to_sql(
        "sales",
        connection,
        if_exists="replace",  # Replace the table each run
        index=False
    )

    connection.close()

    logging.info("Data loaded into SQLite successfully")

# setting up logging configuration
def setup_logging(log_file):
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

#ETL function to extract data from CSV file
def extract(input_file):
    logging.info("Extracting data...")
    df = pd.read_csv(input_file)
    logging.info(f"Loaded {len(df)} records")
    return df

# validate the data
# -------------------------------
# Validate
# -------------------------------
def validate(df):
    logging.info("Validating data...")

    # Required columns
    required_columns = [
        "OrderID",
        "Customer",
        "Product",
        "Quantity",
        "Price"
    ]

    # Check if any required column is missing
    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Ensure Quantity and Price are numeric
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="raise")
    df["Price"] = pd.to_numeric(df["Price"], errors="raise")

    logging.info("Validation successful")

    return df
# Transforming the data
def transform(df):
    logging.info("Transforming data...")

    df = df.drop_duplicates()
    df = df.dropna()

    df["Total"] = df["Quantity"] * df["Price"]
    df["Customer"] = df["Customer"].str.upper()

    return df

# Loading the data into a new CSV file
def load(df, output_file):
    logging.info("Saving cleaned data...")
    df.to_csv(output_file, index=False)

# main
def main():
    config = load_config()

    setup_logging(config["log_file"])

    logging.info("ETL Pipeline Started")

    df = extract(config["input_file"])
    df = transform(df)
    df = validate(df)
    load(df, config["output_file"])
    load_to_database(df, config["database_file"])
    run_analytics(config["database_file"])
    generate_report(config["database_file"])
    generate_chart(config["database_file"])

    logging.info("ETL Pipeline Finished")

    print("ETL Pipeline completed successfully!")


if __name__ == "__main__":
    main()