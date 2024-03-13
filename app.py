from src.ML_project.logger import logging
from src.ML_project.exceptions import CustomExpection
import sys
from src.ML_project.components.data_ingestion import Dataingestion
from src.ML_project.components.data_ingestion import Dataingestionclass
from src.ML_project.components.data_transformation import DataTransformationconfig,DataTransformation

if __name__ == "__main__":
    logging.info("The execution has Started")
    
    try:
        dataingestion = Dataingestion()
        train_data_path, test_data_path = dataingestion.initiate_data_ingestion()
        #data_transformation_config = DataTransformationconfig()
        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path, test_data_path)
    except Exception as ex:
        logging.info("Custom Exception")
        raise CustomExpection(ex, sys)