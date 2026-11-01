from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data"
TABLE_NAMES = ["zip_year", "buildings", "building_months", "hour_profile", "factor_profile"]


def load_tables():
    """Load the 5 tables once: real data if exported, else sample data."""
    folder = DATA / "processed"
    if not (folder / "zip_year.parquet").exists():
        folder = DATA / "sample"
    return {name: pd.read_parquet(folder / f"{name}.parquet")
            for name in TABLE_NAMES if (folder / f"{name}.parquet").exists()}


TABLES = load_tables()