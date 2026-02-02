import os
import pandas as pd
from sqlalchemy import create_engine

def run(input_csv, db_path="data/processed/data.db", table_name="orders"):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    df = pd.read_csv(input_csv)
    print(f"Laddade {len(df)} rader från {input_csv}")
    engine = create_engine(f"sqlite:///{db_path}")
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print("Sparad till", db_path)