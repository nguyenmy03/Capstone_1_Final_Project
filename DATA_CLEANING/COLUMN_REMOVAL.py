import pandas as pd
from pathlib import Path

# ----------------------------------------------------
# 1. Set up paths (works no matter where you run it)
# ----------------------------------------------------
# This file: DATA_CLEANING/COLUMN_REMOVAL.py
this_file = Path(__file__).resolve()

# Project root folder = one level up from DATA_CLEANING
project_root = this_file.parents[1]

# Input CSV is in: <project_root>/data/Most Streamed Spotify Songs 2024.csv
input_path = project_root / "data" / "Most Streamed Spotify Songs 2024.csv"

# Output cleaned CSV
output_path = project_root / "data" / "spotify_2024_cleaned.csv"

print(f"Reading data from: {input_path}")

# ----------------------------------------------------
# 2. Read the CSV
# ----------------------------------------------------
df = pd.read_csv(input_path, encoding="latin1")

# ----------------------------------------------------
# 3. Columns to KEEP (with new cleaned names)
# ----------------------------------------------------
keep_columns = {
    "Track": "Track",
    "Album Name": "Album_Name",
    "Artist": "Artist",
    "Release Date": "Release_Date",
    "All Time Rank": "All_Time_Spotify_Rank",
    "Track Score": "Track_Score",
    "Spotify Streams": "Spotify_Streams",
    "Spotify Popularity": "Spotify_Popularity",
    "YouTube Views": "YouTube_Views",
    "YouTube Likes": "YouTube_Likes",
    "Explicit Track": "Explicit_Track_Ratings",
    "Shazam Counts": "Shazam_Counts",
}

# All existing columns
all_columns = df.columns.tolist()

# Columns that will be kept (intersection of dict keys and actual columns)
cols_to_keep = [c for c in keep_columns.keys() if c in all_columns]

# Columns that will be removed (for your write-up)
removed_columns = [c for c in all_columns if c not in keep_columns.keys()]

# ----------------------------------------------------
# 4. Subset + rename
# ----------------------------------------------------
df = df[cols_to_keep]
df = df.rename(columns=keep_columns)

# ----------------------------------------------------
# 5. Drop rows with undefined / NaN values
# ----------------------------------------------------
df = df.dropna()

# ----------------------------------------------------
# 6. Save cleaned dataset
# ----------------------------------------------------
output_path.parent.mkdir(exist_ok=True, parents=True)
df.to_csv(output_path, index=False)

print("\n🎉 Dataset cleaned successfully!")
print(f"Cleaned file saved to: {output_path}\n")

print("✅ Columns kept (after renaming):")
print(list(df.columns))

print("\n🗑️ Columns removed:")
for col in removed_columns:
    print("-", col)
