from pathlib import Path

# Chemins
ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"
SAMPLE_DIR = DATA_DIR / "sample"
OUTPUT_DIR = ROOT / "outputs"

# Colonnes à charger (Optimisation mémoire)
USECOLS = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime",
    "passenger_count",
    "trip_distance",
    "PULocationID",
    "DOLocationID",
    "payment_type",
    "fare_amount",
    "total_amount",
]

# Types de données (Optimisation mémoire)
DTYPES = {
    "passenger_count": "int8",
    "trip_distance": "float32",
    "PULocationID": "int16",
    "DOLocationID": "int16",
    "payment_type": "int8",
    "fare_amount": "float32",
    "total_amount": "float32",
}