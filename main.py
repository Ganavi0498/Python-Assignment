from src.data_loader import (
    TrainingDataLoader, IdealDataLoader, TestDataLoader
)
from src.database import DatabaseManager
from src.model_selection import ModelSelector
from src.test_mapper import TestMapper
from src.visualizer import Visualizer

def main():
    # 1) Load data
    train_df = TrainingDataLoader("train.csv").load()
    ideal_df = IdealDataLoader("ideal.csv").load()
    test_df  = TestDataLoader("test.csv").load()

    # 2) Persist raw tables to SQLite
    db = DatabaseManager("sqlite:///data.db")
    db.to_sql(train_df, "training_data")
    db.to_sql(ideal_df, "ideal_functions")

    # 3) Select best 4 ideal functions
    selector = ModelSelector(train_df, ideal_df)
    selections, max_devs = selector.select()

    # 4) Map test data
    mapper = TestMapper(test_df, ideal_df, selections, max_devs)
    test_map_df = mapper.map()

    # ———> Insert renaming here to match your assignment schema:
    test_map_df = test_map_df.rename(columns={
        "x":          "X (test func)",
        "y":          "Y (test func)",
        "delta_y":    "Delta Y (test func)",
        "ideal_func": "No. of ideal func"
    })

    # 4b) Persist the renamed output table
    db.to_sql(test_map_df, "test_mapping", if_exists="replace")

    # (Optional) export to CSV for inspection
    test_map_df.to_csv("test_mapping.csv", index=False)

    # 5) Visualize
    viz = Visualizer(train_df, ideal_df, selections)
    viz.plot_training()
    viz.plot_test_mapping(test_map_df)

if __name__ == "__main__":
    main()
