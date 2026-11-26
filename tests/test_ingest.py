import pandas as pd
import pytest
from taxitrips.ingest import load_trips
from taxitrips.config import USECOLS

def test_load_trips_columns(tmp_path):
    # Créer un faux fichier parquet pour le test
    df_mock = pd.DataFrame({
        "tpep_pickup_datetime": ["2024-01-01 10:00:00"],
        "tpep_dropoff_datetime": ["2024-01-01 10:30:00"],
        "passenger_count": [1],
        "trip_distance": [2.5],
        "PULocationID": [100],
        "DOLocationID": [200],
        "payment_type": [1],
        "fare_amount": [15.0],
        "total_amount": [18.0],
        "extra_col_to_drop": ["ignore_me"] # Cette colonne ne doit pas être lue
    })
    dummy_path = tmp_path / "dummy.parquet"
    df_mock.to_parquet(dummy_path)

    # Exécuter la fonction
    df_result = load_trips(dummy_path)

    # Vérifier que seules les colonnes de USECOLS sont présentes
    assert list(df_result.columns) == USECOLS
    assert "extra_col_to_drop" not in df_result.columns
    assert str(df_result["tpep_pickup_datetime"].dtype).startswith("datetime64")