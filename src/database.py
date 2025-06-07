import pandas as pd
from sqlalchemy import create_engine
from .exceptions import DatabaseError

class DatabaseManager:
    """
    Manages a SQLite database via SQLAlchemy.
    Tables can be written directly from pandas DataFrames.
    """
    def __init__(self, db_url: str = "sqlite:///data.db"):
        self.engine = create_engine(db_url)

    def to_sql(self, df: pd.DataFrame, table_name: str, if_exists: str = "replace"):
        """Write DataFrame to the given table name."""
        try:
            df.to_sql(table_name, self.engine, index=False, if_exists=if_exists)
        except Exception as e:
            raise DatabaseError(f"Failed to write table '{table_name}': {e}")
