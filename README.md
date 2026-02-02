# ETL-projekt - Grönagården

Beskrivning: Detta repo innehåller en ETL-pipeline för [dataset]. 

Hur köra:
1. Skapa virtuell miljö:
   python -m venv .venv
   source .venv/bin/activate 

2. Installera dependencies:
   pip install -r requirements.txt

3. Kör pipeline (train):
   python main.py -i data/raw/train.csv -d data/processed/data.db

4. Kör pipeline (validation, append):
   python main.py -i data/raw/validation.csv -d data/processed/data.db --append

5. KPI-notebook:
   öppna notebooks/kpi.ipynb som läser data från SQLite:
   pd.read_sql("SELECT * FROM orders", engine)

Filstruktur:
- data/raw/: råa csv
- data/processed/: databas och processade filer
- src/: pythonkod för pipeline
- notebooks/: EDA och KPI

Data dictionary: data_dictionary.md