from src.mlops1_data_science_project.config.configuration import ConfigurationManager
from src.mlops1_data_science_project.components.data_ingestion import DataIngestion
from src.mlops1_data_science_project import logger

class DataIngestionPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        try:
            config=ConfigurationManager()
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion=DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e
        
if __name__=="__main__":
    logger.info("Starting data ingestion")
    obj=DataIngestionPipeline()
    obj.initiate_data_ingestion()
    logger.info("Data Ingestion completed successfully")