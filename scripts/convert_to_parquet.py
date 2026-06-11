from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).parent.parent


def main():
    df = load_customer_metrics()
    print(f"Loaded {len(df):,} rows")
    write_parquet(df)


def load_customer_metrics():
    return pd.read_csv(PROJECT_ROOT / "data" / "processed" / "customer_metrics.csv")


def write_parquet(df):
    output_path = PROJECT_ROOT / "data" / "processed" / "customer_metrics.parquet"
    df.to_parquet(output_path, engine="pyarrow", index=False)
    print(f"Saved parquet file to {output_path}")


if __name__ == "__main__":
    main()
