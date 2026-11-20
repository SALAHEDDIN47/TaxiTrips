import pandas as pd

def compute_trip_stats(df: pd.DataFrame) -> dict:
    """
    Calcule les statistiques de base sur les trajets.
    """
    # Calcul de la durée en minutes
    df["duration_min"] = (df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]).dt.total_seconds() / 60
    
    stats = {
        "n_trips": len(df),
        "avg_distance": float(df["trip_distance"].mean()),
        "avg_duration_min": float(df["duration_min"].mean()),
        "avg_fare": float(df["fare_amount"].mean()),
        "pax_distribution": df["passenger_count"].value_counts()
    }
    return stats