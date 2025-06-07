import pandas as pd
from .exceptions import DataLoadError

class BaseDataLoader:
    """Base class for loading CSV data into a DataFrame."""
    def __init__(self, filepath: str):
        self.filepath = filepath

    def load(self) -> pd.DataFrame:
        """Read CSV and return a pandas DataFrame."""
        try:
            return pd.read_csv(self.filepath)
        except Exception as e:
            raise DataLoadError(f"Failed to load {self.filepath}: {e}")

class TrainingDataLoader(BaseDataLoader):
    """Loads train.csv (x, y1–y4)."""
    pass  # Inherits load()

class IdealDataLoader(BaseDataLoader):
    """Loads ideal.csv (x, y1–y50)."""
    pass

class TestDataLoader(BaseDataLoader):
    """Loads test.csv (x, y)."""
    pass
