
import pandas as pd
from pathlib import Path
import sys

RAW = Path("data/raw/winemag-data-130k-v2.csv")
if not RAW.exists():
    print("[WARN] Raw CSV not found at", RAW)
    print("Please put the file in data/raw/ or run scripts/00_download_data.py if you have Kaggle credentials.")
    sys.exit(0)

df = pd.read_csv(RAW, index_col=0)
print("shape:", df.shape)
print("\ninfo():")
print(df.info())
print("\nnull counts (top 20):")
print(df.isnull().sum().sort_values(ascending=False).head(20))
print("\npoints describe:")
print(df['points'].describe())
print("\nprice describe (may have NaN):")
print(df['price'].describe())
print("\nTop 10 countries:")
print(df['country'].value_counts().head(10))

# Save a small report
report_path = Path("data/processed/data_check_report.txt")
report_path.parent.mkdir(parents=True, exist_ok=True)
with report_path.open("w", encoding="utf-8") as f:
    f.write(f"shape: {df.shape}\n\n")
    f.write("null counts (top 20):\n")
    f.write(df.isnull().sum().sort_values(ascending=False).head(20).to_string())
print("\nReport saved to", report_path)
