
import pandas as pd


def load_ccd_data(csv_path):
    df = pd.read_csv(csv_path)
    return df


def summarize_growth(df):
    avg_growth_rate = df["growth_rate_h-1"].mean()
    fastest_experiment = df.loc[df["growth_rate_h-1"].idxmax(), "experiment"]
    return avg_growth_rate, fastest_experiment


def summarize_retention(df):
    best_retention_row = df.loc[df["plasmid_retention_harvest_pct"].idxmax()]
    best_experiment = best_retention_row["experiment"]
    best_retention_value = best_retention_row["plasmid_retention_harvest_pct"]
    return best_experiment, best_retention_value


if __name__ == "__main__":
    df = load_ccd_data("data/ccd_design.csv")
    print(df)

    avg_growth_rate, fastest_experiment = summarize_growth(df)
    print("Average growth rate:", avg_growth_rate)
    print("Fastest growing experiment:", fastest_experiment)

    best_experiment, best_retention_value = summarize_retention(df)
    print("Best plasmid retention at harvest:", best_experiment, "with", best_retention_value, "%")