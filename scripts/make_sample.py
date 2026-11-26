import pandas as pd
from pathlib import Path

# Chemins relatifs à la racine du projet
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "raw" / "yellow_tripdata_2024-01.parquet"
DST = ROOT / "data" / "sample" / "trips_sample.parquet"
N = 10_000

def main() -> None:
    if not SRC.exists():
        print(f"Erreur: Le fichier {SRC} n'existe pas. Téléchargez-le depuis le site TLC.")
        return

    print(f"Lecture de {SRC}...")
    df = pd.read_parquet(SRC)
    
    print(f"Prélèvement de {N} lignes...")
    sample = df.sample(n=N, random_state=42).reset_index(drop=True)
    
    DST.parent.mkdir(parents=True, exist_ok=True)
    sample.to_parquet(DST, index=False)
    print(f"✅ Échantillon créé : {DST} ({DST.stat().st_size / 1024:.0f} Ko)")

if __name__ == "__main__":
    main()