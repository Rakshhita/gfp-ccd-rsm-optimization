import pandas as pd


def load_purification_data(csv_path):
    df = pd.read_csv(csv_path)
    return df


def summarize_purification(df):
    eluate_rows = df[df["sample_stage"] == "Eluate"]
    summary = eluate_rows[["experiment", "purification_fold", "yield_pct"]]
    return summary


if __name__ == "__main__":
    df = load_purification_data("data/purification_table.csv")
    print(df)

    summary = summarize_purification(df)
    print(summary)