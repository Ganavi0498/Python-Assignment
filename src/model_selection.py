import numpy as np
import pandas as pd

class BaseSelector:
    """Abstract base for selecting ideal functions."""
    def __init__(self, train_df: pd.DataFrame, ideal_df: pd.DataFrame):
        self.train_df = train_df
        self.ideal_df = ideal_df

    def select(self):
        raise NotImplementedError

class ModelSelector(BaseSelector):
    """
    Matches each of the 4 training curves (y1–y4) to the best-fitting
    ideal function (out of y1–y50) via least-squares.
    """
    def select(self):
        selections = {}
        max_devs = {}
        # assume columns 'y1'..'y4' in train_df; 'x' shared
        for train_col in [c for c in self.train_df.columns if c.startswith("y")]:
            y_train = self.train_df[train_col].values
            sse = {}
            for ideal_col in [c for c in self.ideal_df.columns if c.startswith("y")]:
                y_ideal = self.ideal_df[ideal_col].values
                sse[ideal_col] = np.sum((y_train - y_ideal) ** 2)
            # pick ideal_col with smallest SSE
            best = min(sse, key=sse.get)
            selections[train_col] = best
            # record maximum abs deviation on training set
            max_devs[train_col] = float(np.max(np.abs(y_train - self.ideal_df[best].values)))
        return selections, max_devs
