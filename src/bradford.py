import pandas as pd
from scipy import stats


def fit_standard_curve(csv_path):
    df = pd.read_csv(csv_path)
    x = df["concentration_ug_ul"]
    y = df["absorbance_595nm"]
    result = stats.linregress(x, y)
    slope = result.slope
    intercept = result.intercept
    r_squared = result.rvalue ** 2
    return slope, intercept, r_squared


def absorbance_to_concentration(absorbance, slope, intercept):
    concentration = (absorbance - intercept) / slope
    return concentration


if __name__ == "__main__":
    slope, intercept, r_squared = fit_standard_curve("data/bradford_standards.csv")
    print("Slope:", slope)
    print("Intercept:", intercept)
    print("R-squared:", r_squared)

    test_absorbance = 0.25
    result_concentration = absorbance_to_concentration(test_absorbance, slope, intercept)
    print("Concentration for absorbance", test_absorbance, "is:", result_concentration)
