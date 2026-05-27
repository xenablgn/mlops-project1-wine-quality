from src.mlops1_data_science_project import logger
from src.mlops1_data_science_project.components.data_validation import DataValidation
from src.mlops1_data_science_project.config.configuration import ConfigurationManager


class DataValidationPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e


if __name__ == "__main__":
    logger.info("Starting data validation")
    obj = DataValidationPipeline()
    obj.initiate_data_validation()
    logger.info("Data Validation completed successfully")
