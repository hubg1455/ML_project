import sys
from housing.entity.config_entity import DataIngestionConfig

from housing.exception import HousingException

class DataIngestion:

    def __init__(self,data_ingestion_config=DataIngestionConfig):
        
        try:
            pass

        except Exception as e:
            raise HousingException(e,sys) from e
        