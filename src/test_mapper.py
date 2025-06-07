import numpy as np
import pandas as pd

class TestMapper:
    """
    Maps each test-point (x,y) to one of the four selected ideal functions
    if |y - y_ideal| <= max_dev * sqrt(2). Returns a DataFrame of mappings.
    """
    def __init__(
        self,
        test_df: pd.DataFrame,
        ideal_df: pd.DataFrame,
        selections: dict,
        max_devs: dict
    ):
        self.test_df = test_df
        self.ideal_df = ideal_df.set_index("x")
        self.selections = selections
        self.max_devs = max_devs

    def map(self) -> pd.DataFrame:
        records = []
        for _, row in self.test_df.iterrows():
            x_val, y_val = row["x"], row["y"]
            best = None
            best_dev = None
            # try each training → ideal mapping
            for train_col, ideal_col in self.selections.items():
                if x_val not in self.ideal_df.index:
                    continue
                y_ideal = float(self.ideal_df.loc[x_val, ideal_col])
                dev = abs(y_val - y_ideal)
                threshold = self.max_devs[train_col] * np.sqrt(2)
                if dev <= threshold and (best_dev is None or dev < best_dev):
                    best_dev = dev
                    best = ideal_col
            if best is not None:
                records.append({
                    "x": x_val,
                    "y": y_val,
                    "delta_y": best_dev,
                    "ideal_func": best
                })
        return pd.DataFrame(records)
