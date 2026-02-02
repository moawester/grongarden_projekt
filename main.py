from dotenv import load_dotenv 
import os
load_dotenv()
print("GROQ_API_KEY=", os.getenv("GROQ_API_KEY"))

import argparse
from src.run_pipeline import run

def cli():
    p = argparse.ArgumentParser(description="Kör ETL-pipeline")
    p.add_argument("--input", "-i", required=False, help="Sökväg till raw CSV")
    p.add_argument("--db", "-d", default="data/processed/data.db", help="Output SQLite DB")
    p.add_argument("--table", "-t", default="orders", help="Tabellnamn i SQLite")
    args = p.parse_args()

    input_path = args.input
    if not input_path:
        input_path = input("Skriv sökväg till CSV (t.ex. data/raw/train.csv): ").strip()

    if not os.path.exists(input_path):
        print(f"Fel: input-filen hittades inte: {input_path}")
        exit(1)

    run(input_path, args.db, table_name=args.table)

if __name__ == "__main__":
    cli()