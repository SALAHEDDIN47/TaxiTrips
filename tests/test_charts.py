import pandas as pd
from pathlib import Path
from taxitrips.charts import plot_distance_distribution, plot_trips_by_hour

def test_plot_functions(tmp_path):
    # Faux DataFrame
    df_mock = pd.DataFrame({
        "tpep_pickup_datetime": pd.to_datetime(["2024-01-01 10:00:00", "2024-01-01 14:00:00"]),
        "trip_distance": [2.5, 5.0]
    })
    
    # Tester le premier graphique
    out_dist = tmp_path / "dist.png"
    plot_distance_distribution(df_mock, out_dist)
    assert out_dist.exists()
    
    # Tester le deuxième graphique
    out_hour = tmp_path / "hours.png"
    plot_trips_by_hour(df_mock, out_hour)
    assert out_hour.exists()