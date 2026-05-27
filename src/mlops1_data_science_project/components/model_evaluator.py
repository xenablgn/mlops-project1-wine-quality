from pathlib import Path
from urllib import parse as urlparse

import joblib
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from src.mlops1_data_science_project.entity.config_entity import ModelEvaluationConfig
from src.mlops1_data_science_project.utils.common import save_json


class ModelEvaluator:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, y_true, y_pred):
        # Keep compatibility across sklearn versions where `squared` may be unavailable.
        rmse = mean_squared_error(y_true, y_pred) ** 0.5
        r2 = r2_score(y_true, y_pred)
        mae = mean_absolute_error(y_true, y_pred)

        return rmse, r2, mae

    def log_mlflow(self):
        model = joblib.load(self.config.model_path)
        test_df = pd.read_csv(self.config.test_data_path)

        test_x = test_df.drop(self.config.target_column, axis=1)
        text_y = test_df[self.config.target_column]

        mlflow.set_tracking_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse.urlparse(mlflow.get_tracking_uri()).scheme

        mlflow.set_experiment("Wine Quality Prediction")

        with mlflow.start_run(run_name="Model Evaluation"):
            y_pred = model.predict(test_x)

            rmse, r2, mae = self.eval_metrics(text_y, y_pred)
            scores = {"rmse": rmse, "r2": r2, "mae": mae}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_param("model_path", self.config.model_path)
            mlflow.log_param("test_data_path", self.config.test_data_path)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)

            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(
                    model, "model", registered_model_name="WineQualityModel"
                )
            else:
                mlflow.sklearn.log_model(model, "model")
