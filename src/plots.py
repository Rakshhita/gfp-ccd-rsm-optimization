import pandas as pd
import matplotlib.pyplot as plt


def plot_growth_rate(csv_path, output_path):
    df = pd.read_csv(csv_path)

    plt.figure(figsize=(8, 5))
    plt.bar(df["experiment"], df["growth_rate_h-1"], color="steelblue")
    plt.xlabel("Experiment")
    plt.ylabel("Growth Rate (h-1)")
    plt.title("Specific Growth Rate by Experiment")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_plasmid_retention(csv_path, output_path):
    df = pd.read_csv(csv_path)

    x = range(len(df["experiment"]))
    width = 0.25

    plt.figure(figsize=(9, 5))
    plt.bar([i - width for i in x], df["plasmid_retention_inoculation_pct"], width=width, label="Inoculation", color="#4C72B0")
    plt.bar(x, df["plasmid_retention_induction_pct"], width=width, label="Induction", color="#55A868")
    plt.bar([i + width for i in x], df["plasmid_retention_harvest_pct"], width=width, label="Harvest", color="#C44E52")

    plt.xticks(list(x), df["experiment"])
    plt.xlabel("Experiment")
    plt.ylabel("Plasmid Retention (%)")
    plt.title("Plasmid Retention Across Experimental Stages")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_purification_summary(csv_path, output_path):
    df = pd.read_csv(csv_path)
    eluate_rows = df[df["sample_stage"] == "Eluate"]

    x = range(len(eluate_rows["experiment"]))
    width = 0.35

    fig, ax1 = plt.subplots(figsize=(8, 5))
    bar1 = ax1.bar([i - width / 2 for i in x], eluate_rows["purification_fold"], width=width, label="Purification Fold", color="#8172B2")
    ax1.set_ylabel("Purification Fold")
    ax1.set_xticks(list(x))
    ax1.set_xticklabels(eluate_rows["experiment"])

    ax2 = ax1.twinx()
    bar2 = ax2.bar([i + width / 2 for i in x], eluate_rows["yield_pct"], width=width, label="Yield %", color="#CCB974")
    ax2.set_ylabel("Yield (%)")

    bars = [bar1, bar2]
    labels = [b.get_label() for b in bars]
    ax1.legend(bars, labels, loc="upper right")

    plt.title("Purification Fold vs Yield Trade-off (Eluate Stage)")
    fig.tight_layout()
    plt.savefig(output_path)
    plt.close()


if __name__ == "__main__":
    plot_growth_rate("data/ccd_design.csv", "growth_rate_plot.png")
    print("Saved plot to growth_rate_plot.png")

    plot_plasmid_retention("data/ccd_design.csv", "plasmid_retention_plot.png")
    print("Saved plot to plasmid_retention_plot.png")

    plot_purification_summary("data/purification_table.csv", "purification_plot.png")
    print("Saved plot to purification_plot.png")
