import pandas as pd
import statsmodels.formula.api as smf


def load_data(csv_path):
    df = pd.read_csv(csv_path)
    return df


def fit_first_order_model(df):
    """
    Fits a simplified First Order regression model.

    NOTE: The original dissertation used a 5-factor Central Composite
    Design across 44 experiments (11 teams x 4 runs) to have enough
    data points to estimate all factors reliably. This project only
    has the 4 summary experiments explicitly reported in the write-up,
    so fitting all 5 factors at once is mathematically underdetermined
    (more unknowns than data points). We instead demonstrate the same
    RSM regression method using the two factors the dissertation
    itself identified as most significant: IPTG concentration and
    temperature.
    """
    model = smf.ols("Q('growth_rate_h-1') ~ temp_C + IPTG_uM", data=df)
    result = model.fit()
    return result


def fit_two_way_interaction_model(df):
    """
    Fits a Two-Way Interaction (TWI) model, adding a term for
    temp_C * IPTG_uM to check whether the two factors combined
    have an effect beyond their individual contributions.
    """
    model = smf.ols("Q('growth_rate_h-1') ~ temp_C * IPTG_uM", data=df)
    result = model.fit()
    return result


if __name__ == "__main__":
    df = load_data("data/ccd_design.csv")
    print(df)

    print("\n===== FIRST ORDER MODEL =====")
    fo_result = fit_first_order_model(df)
    print(fo_result.summary())

    print("\n===== TWO-WAY INTERACTION MODEL =====")
    twi_result = fit_two_way_interaction_model(df)
    print(twi_result.summary())
EO

exit
cd ~/Desktop/gfp-ccd-rsm-optimization
pwd


