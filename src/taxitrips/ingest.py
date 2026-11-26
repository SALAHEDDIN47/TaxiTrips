import pandas as pd
from pathlib import Path
from .config import USECOLS, DTYPES

def load_trips(path: Path | str) -> pd.DataFrame:
    """
    Charge le fichier Parquet des trajets de taxi de manière optimisée.
    """
    df = pd.read_parquet(path, columns=USECOLS, engine="pyarrow")
    df = df.astype(DTYPES)
    df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
    df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])
    return df