from src.mlops1_data_science_project import logger
from src.mlops1_data_science_project.components.data_transformation import (
    DataTransformation,
)
from src.mlops1_data_science_project.config.configuration import ConfigurationManager


class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open("artifacts/data_validation/status.txt") as f:
                validation_status = f.read().split(":")[-1].strip()
            if validation_status != "True":
                raise Exception(
                    "Data validation failed. Cannot proceed with data transformation."
                )
            else:
                logger.info(
                    "Data validation successful. Proceeding with data transformation."
                )
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(
                    config=data_transformation_config
                )
                data_transformation.train_test_splitting()
        except Exception as e:
            logger.exception(e)
            raise e


if __name__ == "__main__":
    logger.info("Starting data transformation")
    obj = DataTransformationPipeline()
    obj.initiate_data_transformation()
    logger.info("Data Transformation completed successfully")
