#!/usr/bin/env python3
# assgn5/filter_columns.py
# Purpose: Keep only selected columns and save a cleaned CSV for the pipeline

import pandas as pd
from pathlib import Path

# === 1) Define source and output paths ===
SRC = Path("data/assgn5_sample.csv")          # your original CSV
OUT = Path("data/assgn5_sample_filtered.csv") # new filtered file

# === 2) Define columns to KEEP ===
KEPT = [
    "Academic Year",
    "County Name",
    "District Name",
    "School Name",
    "School Type",
    "Status",
    "Open Date",
    "City",
    "Zip",
    "Latitude",
    "Longitude",
    "Enroll Total",
    "African American (%)",
    "Hispanic (%)",
    "Asian (%)"
]

# === 3) Load the CSV ===
if not SRC.exists():
    raise SystemExit(f"[Error] Source file not found: {SRC}")

df = pd.read_csv(SRC, low_memory=False)
print(f"[OK] Loaded dataset with {len(df)} rows and {len(df.columns)} columns.")

# === 4) Filter columns ===
missing = [c for c in KEPT if c not in df.columns]
if missing:
    print(f"[Warning] These columns were not found and will be skipped: {missing}")

df_filtered = df[[c for c in KEPT if c in df.columns]]
print(f"[OK] Keeping {len(df_filtered.columns)} columns: {list(df_filtered.columns)}")

# === 5) Save the filtered CSV ===
OUT.parent.mkdir(parents=True, exist_ok=True)
df_filtered.to_csv(OUT, index=False, encoding="utf-8")
print(f"[OK] Saved cleaned dataset to: {OUT.resolve()}")
print(f"[INFO] Final shape: {df_filtered.shape}")
