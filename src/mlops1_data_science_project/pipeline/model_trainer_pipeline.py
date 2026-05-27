from src.mlops1_data_science_project import logger
from src.mlops1_data_science_project.components.model_trainer import ModelTrainer
from src.mlops1_data_science_project.config.configuration import ConfigurationManager


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        try:
            config_manager = ConfigurationManager()
            model_trainer_config = config_manager.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()
        except Exception as e:
            logger.exception(e)
            raise e
