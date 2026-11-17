import urllib.request
from pathlib import Path

URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"
DST = Path("data/raw/yellow_tripdata_2024-01.parquet")

def main():
    DST.parent.mkdir(parents=True, exist_ok=True)
    if not DST.exists():
        print(f"Téléchargement de {URL}...")
        urllib.request.urlretrieve(URL, DST)
        print("✅ Terminé.")
    else:
        print("Le fichier existe déjà.")

if __name__ == "__main__":
    main()