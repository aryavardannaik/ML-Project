from src.ML_project.logger import logging
from src.ML_project.exceptions import CustomExpection
import sys
from src.ML_project.components.data_ingestion import Dataingestion
from src.ML_project.components.data_ingestion import Dataingestionclass


if __name__ == "__main__":
    logging.info("The execution has Started")
    
    try:
        dataingestion = Dataingestion()
        dataingestion.initiate_data_ingestion()
    except Exception as ex:
        logging.info("Custom Exception")
        raise CustomExpection(ex, sys)