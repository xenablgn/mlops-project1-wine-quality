from src.mlops1_data_science_project import logger
from src.mlops1_data_science_project.components.model_evaluator import ModelEvaluator
from src.mlops1_data_science_project.config.configuration import ConfigurationManager


class ModelEvaluatorPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            config_manager = ConfigurationManager()
            model_eval_config = config_manager.get_model_eval_config()
            model_evaluator = ModelEvaluator(config=model_eval_config)
            model_evaluator.log_mlflow()
        except Exception as e:
            logger.exception(e)
            raise e
