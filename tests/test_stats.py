import pandas as pd
from taxitrips.stats import compute_trip_stats

def test_compute_trip_stats():
    # Créer un faux DataFrame
    df_mock = pd.DataFrame({
        "tpep_pickup_datetime": pd.to_datetime(["2024-01-01 10:00:00", "2024-01-01 11:00:00"]),
        "tpep_dropoff_datetime": pd.to_datetime(["2024-01-01 10:30:00", "2024-01-01 11:15:00"]),
        "trip_distance": [2.0, 4.0],
        "fare_amount": [10.0, 20.0],
        "passenger_count": [1, 2]
    })
    
    stats = compute_trip_stats(df_mock)
    
    assert stats["n_trips"] == 2
    assert stats["avg_distance"] == 3.0
    assert stats["avg_duration_min"] == 22.5  # (30 + 15) / 2
    assert stats["avg_fare"] == 15.0