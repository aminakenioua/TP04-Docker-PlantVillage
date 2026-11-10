import os
import pandas as pd

DATA_PATH = "/app/data/PlantVillage_PowerBI.csv"

print("=== TP04 Docker Data Analysis ===")

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

df = pd.read_csv(DATA_PATH)

print(f"Dataset: {os.path.basename(DATA_PATH)}")
print(f"Number of rows: {len(df)}")
print(f"Number of columns: {len(df.columns)}")

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head().to_string(index=False))

print("\nAnalysis completed successfully!")
