import subprocess
import zipfile
from pathlib import Path

# ✅ This is the exact Kaggle dataset you chose
DATASET_SLUG = "nelgiriyewithana/most-streamed-spotify-songs-2024"

def download_and_unzip(slug: str = DATASET_SLUG, dest_dir: str = "data") -> None:
    """
    Download the 'Most Streamed Spotify Songs 2024' dataset from Kaggle
    using the Kaggle CLI, then unzip it into a local folder.
    """
    dest = Path(dest_dir)
    dest.mkdir(exist_ok=True)

    print(f"Downloading Kaggle dataset: {slug}")
    cmd = [
        "kaggle", "datasets", "download",
        "-d", slug,
        "-p", str(dest),
        "--force"
    ]

    # Run the Kaggle command
    subprocess.run(cmd, check=True)
    print("✔ Download finished.")

    # Find any ZIP files in the destination folder
    zip_files = list(dest.glob("*.zip"))
    if not zip_files:
        print("❌ No .zip file found in", dest)
        return

    # Unzip all found archives
    for z in zip_files:
        print(f"Unzipping {z.name}...")
        with zipfile.ZipFile(z, "r") as zip_ref:
            zip_ref.extractall(dest)
        print(f"✔ Unzipped into {dest.resolve()}")

    print("\n🎉 Done! Check the 'data' folder for 'Most Streamed Spotify Songs 2024.csv'.")

if __name__ == "__main__":
    download_and_unzip()
