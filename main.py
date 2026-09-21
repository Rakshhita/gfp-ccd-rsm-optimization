from src.bradford import fit_standard_curve, absorbance_to_concentration
from src.growth_retention import load_ccd_data, summarize_growth, summarize_retention
from src.purification import load_purification_data, summarize_purification
from src.rsm_model import load_data, fit_first_order_model, fit_two_way_interaction_model
from src.plots import plot_growth_rate, plot_plasmid_retention, plot_purification_summary


def main():
    print("=" * 60)
    print("GFP EXPRESSION OPTIMISATION - FULL ANALYSIS PIPELINE")
    print("=" * 60)

    print("\n--- Bradford Assay Calibration ---")
    slope, intercept, r_squared = fit_standard_curve("data/bradford_standards.csv")
    print(f"Standard curve: absorbance = {slope:.4f} * concentration + {intercept:.4f}")
    print(f"R-squared: {r_squared:.4f}")

    print("\n--- Growth & Plasmid Retention ---")
    ccd_df = load_ccd_data("data/ccd_design.csv")
    avg_growth, fastest_exp = summarize_growth(ccd_df)
    print(f"Average growth rate: {avg_growth:.4f} h-1")
    print(f"Fastest growing experiment: {fastest_exp}")
    best_exp, best_retention = summarize_retention(ccd_df)
    print(f"Best plasmid retention at harvest: {best_exp} with {best_retention}%")

    print("\n--- Protein Purification Summary ---")
    purification_df = load_purification_data("data/purification_table.csv")
    purification_summary = summarize_purification(purification_df)
    print(purification_summary.to_string(index=False))

    print("\n--- RSM Regression Models ---")
    rsm_df = load_data("data/ccd_design.csv")
    fo_result = fit_first_order_model(rsm_df)
    print(f"First Order model R-squared: {fo_result.rsquared:.4f}")

    print("\n--- Generating Plots ---")
    plot_growth_rate("data/ccd_design.csv", "growth_rate_plot.png")
    plot_plasmid_retention("data/ccd_design.csv", "plasmid_retention_plot.png")
    plot_purification_summary("data/purification_table.csv", "purification_plot.png")
    print("Saved: growth_rate_plot.png, plasmid_retention_plot.png, purification_plot.png")

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
