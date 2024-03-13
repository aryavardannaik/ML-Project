import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.ML_project.exceptions import CustomExpection
from src.ML_project.logger import logging
import os
from src.ML_project.utils import save_object
@dataclass

class DataTransformationconfig:
    preprocessing_file_path = os.path.join('Data_file', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationconfig()
        
    def get_data_transformer_obj(self):
        
        try:
            numerical_columns = [' ',' ']
            categorical_columns = ['','','','']
            num_pipeline = Pipeline(
                steps=[('imputer', SimpleImputer(stratregy= 'median')),
                        ('scaler', StandardScaler())]
            )
            cat_pipeline = Pipeline(
                steps=[('imputer', SimpleImputer(stratregy= 'median')),
                       ('one_hot_encoder', OneHotEncoder),
                       ('scaler', StandardScaler(with_mean= False))]
                
            )
            logging.info(f"Catogorical{categorical_columns}")
            logging.info(f"Numerical{numerical_columns_columns}")
            
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cat_pipeline", cat_pipeline, categorical_columns)
                ])
            return preprocessor
            
        except Exception as e:
            raise CustomExpection(e, sys)
        
        def initiate_dataTransformation(self,train_path, test_path):
            try:
                train_df = pd.read_csv(train_path)
                test_df = pd.read_csv(test_path)
                
                logging.info(f"reading the test and train file")
                processing_obj = self.get_data_transformer_obj(self)
                
                target_column = 'Heart Attack Risk'
                numerical_columns = ''
                categorical_columns = ''
                
                input_features_train_df = train_df.drop(columns=[target_column], axis=1)
                target_feaures_train_df = train_df[target_column]
                
                input_features_test_df = test_df.drop(columns=[target_column], axis=1)
                target_feaures_test_df = test_df[target_column]
                
                logging.info("applying the preprocessing")
                
                input_features_train_arr = preprocessing_obj.fit_transform(input_features_train_df)
                input_features_test_arr = preprocessing_obj.transform(input_features_test_df) 
                
                train_arr = np.c_[
                    input_features_train_arr, np.array(target_feaures_train_df)
                ]
                test_arr = np.c_[input_features_test_arr, np.array(target_feaures_test_df)]
                
                logging.info(f"Saved Preprocessing object")
                save_object(
                    file_path = self.data_trtansformation_config.preprocessor_obj_file_path,
                    obj = processing_obj
                )   
                return (
                    train_arr, test_arr, self.data_transformation_config.preprocessor_obj 
                )
                
                
            except Exception as e:
                raise CustomExpection(e, sys)
                  
    