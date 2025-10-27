"""
## 🧠 Script Usage Instructions

This script (`assgn5/collect_sample.py`) creates a small working sample (≈750–800 rows)
for the A5 pipeline (**collect → model → publish → visualize → explain**).

### ⚙️ How to Run

**Using the local source CSV in this repo:**
    python assgn5/collect_sample.py --input "data/assgn5_source.csv" --output "data/assgn5_sample.csv"

### 📂 Inputs & Outputs
- Input:  data/assgn5_source.csv
- Output: data/assgn5_sample.csv
- Purpose: produce a smaller, reproducible sample for BigQuery → Grafana visualization.
"""

#!/usr/bin/env python3
# assgn5/collect_sample.py
import argparse, os, ssl, tempfile
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
import certifi, pandas as pd

DATA_DIR = Path("data")
OUT_PATH = DATA_DIR / "assgn5_sample.csv"

def ensure_dirs():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def download_https_csv(url: str) -> Path:
    """Download a CSV securely over HTTPS (with certificate validation)."""
    if not url.lower().startswith("https://"):
        raise ValueError("URL must start with https://")
    ctx = ssl.create_default_context(cafile=certifi.where())
    req = Request(url, headers={"User-Agent": "assgn5-collector/1.0"})
    with urlopen(req, context=ctx, timeout=90) as resp, \
         tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        tmp.write(resp.read())
        return Path(tmp.name)

def main():
    ap = argparse.ArgumentParser(description="Validate and save a ~100-row sample from CSV.")
    ap.add_argument("--url", help="HTTPS CSV URL")
    ap.add_argument("--local", help="Local CSV path (if using local file)")
    ap.add_argument("--sample-size", type=int, default=100)
    ap.add_argument("--out", default=str(OUT_PATH))
    args = ap.parse_args()

    ensure_dirs()

    # Prefer local file if provided
    if args.local:
        src = Path(args.local)
        if not src.exists():
            raise SystemExit(f"File not found: {src}")
        df = pd.read_csv(src, low_memory=False)
        print(f"[Info] Loaded local CSV: {src}")
    else:
        url = args.url or os.environ.get("CSV_URL")
        if not url:
            raise SystemExit("Provide either --local PATH or --url HTTPS_URL")
        tmp = download_https_csv(url)
        print(f"[Info] Downloaded temporary file: {tmp}")
        df = pd.read_csv(tmp, low_memory=False)

    print(f"[OK] Total rows in full dataset: {len(df)}")
    if len(df) == 0:
        raise SystemExit("[Error] Empty dataset.")

    n = min(args.sample_size, len(df))
    df_sample = df.sample(n=n, random_state=42)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df_sample.to_csv(out_path, index=False, encoding="utf-8")
    print(f"[OK] Saved {n}-row sample to: {out_path}")

    print("[Preview] First record (dict):")
    print(df.iloc[0].to_dict())

if __name__ == "__main__":
    main()
