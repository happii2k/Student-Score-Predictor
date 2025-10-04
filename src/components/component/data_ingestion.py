import os
import sys 
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.exception.exception import CustomException
from src.components.logger.logger import logging
from src.components.component.data_transforming import DataTransformation

from src.components.component.model_trainer import ModelTrainer

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")   # Use your MongoDB URI
db = client["SchoolData"]
collection = db["data1"]



  #  from src.components.exception import CustomException
   # from src.components.logger import logging
   # from src.components.utils import save_object

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__ (self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion method starts")
        try:
            # Read all documents
            data_cursor = collection.find()
            df = pd.DataFrame(list(data_cursor))
            if '_id' in df.columns:
                 df = df.drop('_id', axis=1)

            df = pd.DataFrame(list(collection.find()))
            print(df.shape)


            logging.info("Dataset read as pandas dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw data is saved")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)


            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
    train_data, test_data = obj.initiate_data_ingestion()

    dataTransformation = DataTransformation()
    dataTransformation.initiate_data_transformation(train_data, test_data)

    Train_ARR , Test_arr , _ = dataTransformation.initiate_data_transformation(train_data, test_data)

    modeltrainer = ModelTrainer()
    modeltrainer.initiate_model_trainer(Train_ARR , Test_arr )

