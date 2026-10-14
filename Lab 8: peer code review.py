# Madison Lowenstein
# October 14, 2026
# Lab 8: peer code review #
# Adding the two improvements of my choice out of the options onm canvas #
# perform regression for certain ranges of data and create a CLI app for plot formatting #
##############################


# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


csv_path = input("Enter the dataset filename: ")

# load dataset
df = pd.read_csv(csv_path)

# Cleans the column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Added the drop names
for column in df.columns:
    if df[column].name == "names":
        df.drop(column, axis=1, inplace=True)

# Displays columns names
print("Available columns:")
print(df.columns.tolist())


# Ask user to select their variables
x_col = input("Enter the X variable: ").strip().lower()
y_col = input("Enter the Y variable: ").strip().lower()


# Makes sure the columns exist
if x_col not in df.columns or y_col not in df.columns:
    print("Error: One or both columns do not exist")
    exit()


# Selects the x and y columns
data = df[[x_col, y_col]].copy()

# Removes any commas and also converts values to numbers
for col in  [x_col, y_col]:
    data[col] = pd.to_numeric(data[col].astype(str).str.replace(",",""),
                errors="coerce")

# Remove rows w/ missing values
data = data.dropna()

# Adding the 2 improvements asked in canvas lab 8

# perform regression for certain ranges of data
filter_choice = input("Do you want to filter the data by a specific range? (y/n): ").strip().lower()
if filter_choice in ["y", "yes"]:
    print("Filtering data")

x_min = input(f"Enter the X min value: {x_col}: ").strip().lower()
x_max = input(f"Enter the X max value: {x_col}: ").strip().lower()
if x_min:
    data = data[data[x_col] >= float(x_min)]
if x_max:
    data = data[data[x_col] <= float(x_max)]

y_min = input(f"Enter the Y min value: {y_col}: ").strip().lower()
y_max = input(f"Enter the Y max value: {y_col}: ").strip().lower()
if y_min:
    data = data[data[y_col] >= float(y_min)]
if y_max:
    data = data[data[y_col] <= float(y_max)]

print(f"data filtered: {len(data)} rows remaining within the specified range")

if len(data) < 2:
    print("error: At least 2 data points required to perform OLS regression. Please restart and choose another range")
    exit()

# create a CLI app interface for plot formatting in the script
print("\nPlot CLI APP ")

color = input("enter the color of plot").strip()
weight = input("enter the weight of plot").strip()
gridline = input("do you want gridlines? (y/n): ").strip().lower()
title = input("enter the title of plot").strip()

try:
    parsed_weight = float(weight) if weight else 2.0
except ValueError:
    parsed_weight = 2.0

plot_config = {
    "color": color if color else "tab:blue",
    "line_weight": parsed_weight,
    "gridlines": gridline in ["y", "yes"],
    "custom_title": title,
}

# Creating the scatterplot
fig, ax = plt.subplots(figsize=(8,6))

ax.scatter(data[x_col], data[y_col], alpha=0.6, edgecolor="k", linewidth=0.3)

ax.set_xlabel(x_col)
ax.set_ylabel(y_col)

initial_title = plot_config["custom_title"] if plot_config["custom_title"] else f"{y_col} vs. {x_col}"
ax.set_title(initial_title)

if plot_config["gridlines"]:
    ax.grid(alpha=0.3)

fig.tight_layout()


# Prompts user to save the scatterplot if they want
save_scatter = input("Do you want to save the scatter plot? (y/n): ").strip().lower()

# Changed it to automatically save the specific filename for the scatter plot saved
if save_scatter == "y":
    filename = f"{x_col}_vs_{y_col}.png"
    fig.savefig(filename + ".png", dpi = 300)
    print("Scatter plot saved")


# Calculates OLS regression
x = sm.add_constant(data[x_col])
model = sm.OLS(data[y_col], x).fit()


# Displays the results
print("\nOlS regression results: ")
print(model.summary())

# Values for regression
x_line = np.linspace(data[x_col].min(), data[x_col].max(), 100)
y_line = model.params["const"] + model.params[x_col] * x_line

# Adds regression line to scatterplot
ax.plot(
x_line,
y_line,
color=plot_config["color"],
linewidth = plot_config["line_weight"],
label=f"OLS Line(R^2 = {model.rsquared:.3f})"
)

ax.legend()

final_title = plot_config["custom_title"] if plot_config["custom_title"] else f"{y_col} vs. {x_col} with OLS regression line"
ax.set_title(final_title)

# Ask the user to save scatterplot
save_ols = input("Do you want to save the OLS plot? (y/n): ").strip().lower()

# Changed the input file name for the OLS plot saved
if save_ols in ["y", "yes"]:
    ols_filename = f"{x_col}_vs_{y_col}.png"
    fig.savefig(ols_filename + ".png", dpi = 300)
    print("OLS plot saved")

plt.show()
