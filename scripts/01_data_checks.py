import pandas as pd
from pathlib import Path

p = Path("data/raw/winemag-data-130k-v2.csv")
if not p.exists():
    print("Raw CSV not found at", p)
else:
    df = pd.read_csv(p, index_col=0)
    print("shape:", df.shape)
    print(df.info())
    print("null counts:\n", df.isnull().sum().sort_values(ascending=False).head(20))
    print("points describe:\n", df['points'].describe())
    print("price describe:\n", df['price'].describe())
    print("top countries:\n", df['country'].value_counts().head(10))