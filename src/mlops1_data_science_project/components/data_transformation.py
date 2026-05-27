from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from src.mlops1_data_science_project import logger
from src.mlops1_data_science_project.entity.config_entity import (
    DataTransformationConfig,
)


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split(self, test_size: float = 0.2, random_state: int = 42):
        data = pd.read_csv(self.config.data_path)
        train_data, test_data = train_test_split(
            data, test_size=test_size, random_state=random_state
        )
        output_dir = Path(self.config.root_dir)
        train_data.to_csv(output_dir / "train_data.csv", index=False)
        test_data.to_csv(output_dir / "test_data.csv", index=False)
        logger.info(f"Train and test data saved at {output_dir}")
        logger.info(
            f"Train data shape: {train_data.shape}, Test data shape: {test_data.shape}"
        )
