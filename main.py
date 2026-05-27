from src.mlops1_data_science_project import logger
from src.mlops1_data_science_project.pipeline.data_ingestion_pipeline import (
    DataIngestionPipeline,
)
from src.mlops1_data_science_project.pipeline.data_transformation_pipeline import (
    DataTransformationPipeline,
)
from src.mlops1_data_science_project.pipeline.data_validation_pipeline import (
    DataValidationPipeline,
)

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    pipeline = DataIngestionPipeline()
    pipeline.initiate_data_ingestion()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    pipeline = DataValidationPipeline()
    pipeline.initiate_data_validation()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    pipeline = DataTransformationPipeline()
    pipeline.initiate_data_transformation()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)

STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    from src.mlops1_data_science_project.pipeline.model_trainer_pipeline import (
        ModelTrainerPipeline,
    )

    pipeline = ModelTrainerPipeline()
    pipeline.initiate_model_trainer()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
