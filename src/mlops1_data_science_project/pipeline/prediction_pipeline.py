from pathlib import Path

import joblib
import numpy as np
import pandas as pd


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))

    def predict(self, input_data: pd.DataFrame) -> np.ndarray:
        predictions = self.model.predict(input_data)

        return predictions
