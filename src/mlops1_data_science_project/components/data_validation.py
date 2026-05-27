import pandas as pd

from src.mlops1_data_science_project import logger
from src.mlops1_data_science_project.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self):
        try:
            validation_status = True

            data = pd.read_csv(self.config.unzip_data_dir)

            all_cols = set(data.columns)
            all_schema_cols = set(self.config.all_schema.keys())

            missing_cols = all_schema_cols - all_cols
            extra_cols = all_cols - all_schema_cols

            with open(self.config.STATUS_FILE, "w") as f:
                if missing_cols:
                    validation_status = False

                    for col in missing_cols:
                        logger.info(f"Missing column in dataset: {col}")
                        f.write(f"Missing column: {col}\n")

                if extra_cols:
                    validation_status = False

                    for col in extra_cols:
                        logger.info(f"Extra column in dataset: {col}")
                        f.write(f"Extra column: {col}\n")

                if validation_status:
                    logger.info("All columns are valid")
                    f.write("Validation status: True\n")
                else:
                    f.write("Validation status: False\n")

            return validation_status

        except Exception as e:
            logger.exception(e)
            raise e
