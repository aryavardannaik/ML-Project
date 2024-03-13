import os
import sys
import pandas as pd
from src.ML_project.logger import logging
from src.ML_project.exceptions import CustomExpection
from dataclasses import dataclass
from src.ML_project.utils import read_SQL_data
from sklearn.model_selection import train_test_split

@dataclass 
class Dataingestionclass:
    train_data_path = os.path.join("Data_file","train.csv")
    test_data_path = os.path.join("Data_file","test.csv")
    raw_data_path = os.path.join("Data_file","raw.csv")
    
class Dataingestion:
    def __init__(self):
        self.ingestion_config = Dataingestionclass()
        
    def initiate_data_ingestion(self):
        try:
            df= read_SQL_data(os.path.join('notbook/data', 'raw.csv'))
            logging.info("Reading Data from MYSQL")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)
            
            df.to_csv(self.ingestion_config.raw_data_path, index= False, header= True)
            
            train_set, test_set = train_test_split(df, test_size= 0.25, random_state= 42)
            train_set.to_csv(self.ingestion_config.train_data_path, index= False, header= True)
            test_set.to_csv(self.ingestion_config.test_data_path, index= False, header= True)
            
            logging.info("data Ingestion is complete")
        except Exception as ex:   
            raise CustomExpection(ex,sys)
        return self.ingestion_config.test_data_path
        self.ingestion_config.train_data_path
