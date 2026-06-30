# importing the libraries 
import pandas as pd
import logging
import os

# setting up logging configuration
logging.basicConfig(filename='logs/pipeline.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('ETL pipeline started.')
