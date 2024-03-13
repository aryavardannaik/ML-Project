import os
import sys
import numpy as np
import pandas as pd
from src.ML_project.logger import logging
from src.ML_project.exceptions import CustomExpection
from dotenv import load_dotenv
import pymysql
import pickle



load_dotenv()
host = os.getenv('host')
username = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')


def read_SQL_data():
    logging.info("Reading SQL Data")
    try:
        mydb = pymysql.connect(
            host = host,
            user = username,
            password = password,
            db = db
        )
        logging.info("Connection Established %s", mydb)
        df = pd.read_sql_query("SELECT * FROM attack",mydb)
        print(df.head())
        return df
    
    except Exception as e:
        raise CustomExpection(e, sys)
    
def save_object(file, obj):
        try:
            dir_path = os.path.dirname(file_path)
            
            os.makedirs(dir_path, exist_ok= True)
            
            with open(file_path, 'wb') as file_obj:
                pickel.dump(obj, file_obj)
                
        except Exception as e:
                raise CustomExpection(e, sys)