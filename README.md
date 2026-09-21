# GFP Expression Optimisation - Data Analysis Pipeline

A Python data analysis project reproducing and extending the statistical
analysis from a real recombinant protein expression optimisation experiment
(GFP expressed in E. coli BL21(DE3), analysed via a Central Composite
Design / Response Surface Methodology approach).

## What this project does

- Bradford assay calibration - fits a linear standard curve and converts
  absorbance readings to protein concentration
- Growth and plasmid retention analysis - compares growth rate and plasmid
  stability across experimental conditions
- Protein purification summary - tracks purification fold and yield
  through Crude Extract, Supernatant, and Eluate stages
- RSM regression modelling - fits First Order and Two-Way Interaction
  regression models using statsmodels
- Visualisations - generates bar charts summarising growth rate, plasmid
  retention, and purification trade-offs

## Data note

The original experiment used a 5-factor, 44-run Central Composite Design
across 11 teams. This project uses the 4 summary experiments explicitly
reported in that write-up. Some data points were back-calculated from a
reported regression equation rather than sourced from raw instrument
output, since raw readings were not available.

## Running it

pip3 install -r requirements.txt
python3 main.py
