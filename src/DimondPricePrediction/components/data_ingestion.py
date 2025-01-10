
import pandas as pd
import numpy as np
from src.Dimondpriceprediction.logger import logging
from src.Dimondpriceprediction.exception import customexception

import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts","raw.csv")
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("data ingestion started")
        
        try:
            
            filepath = Path("notebooks/data") / "Gemstone.csv"
            data = pd.read_csv(filepath)
            logging.info("I have read the dataset as data")
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("I have saved the raw data in artifact folder")
            
            logging.info("Here i have performed train test split")
            train_data,test_data = train_test_split(data,test_size=0.25,random_state=42)
            logging.info("train-test split completed")
            
            train_data.to_csv(self.ingestion_config.train_data_path)
            test_data.to_csv(self.ingestion_config.test_data_path)
            
            logging.info("Data ingestion completed")
            
            return (
                
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
            
            
        except Exception as e:
            logging.info("Exception occured during data ingestion")
            raise customexception(e,sys)