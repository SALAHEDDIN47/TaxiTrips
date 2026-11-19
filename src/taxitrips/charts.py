import matplotlib
matplotlib.use('Agg') # Obligatoire pour éviter les erreurs en CI
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

def plot_distance_distribution(df: pd.DataFrame, output_path: Path | str) -> None:
    """Génère un histogramme de la distribution des distances."""
    plt.figure(figsize=(10, 6))
    # On filtre les distances aberrantes (ex: > 50 miles) pour un plus beau graphique
    df_filtered = df[df["trip_distance"] < 50]
    plt.hist(df_filtered["trip_distance"], bins=50, color='skyblue', edgecolor='black')
    plt.title("Distribution des distances des trajets")
    plt.xlabel("Distance (miles)")
    plt.ylabel("Nombre de trajets")
    plt.grid(axis='y', alpha=0.75)
    
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path)
    plt.close()

def plot_trips_by_hour(df: pd.DataFrame, output_path: Path | str) -> None:
    """Génère un graphique en barres du nombre de trajets par heure."""
    plt.figure(figsize=(10, 6))
    # Extraire l'heure
    hours = df["tpep_pickup_datetime"].dt.hour
    hour_counts = hours.value_counts().sort_index()
    
    plt.bar(hour_counts.index, hour_counts.values, color='coral')
    plt.title("Nombre de trajets par heure de la journée")
    plt.xlabel("Heure (0-23)")
    plt.ylabel("Nombre de trajets")
    plt.xticks(range(0, 24))
    plt.grid(axis='y', alpha=0.75)
    
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path)
    plt.close()