# Madison Lowenstein
# October 12, 2026
# IC # 6/ debug a peer's lab 7
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

# Added the drop rownames
for column in df.columns:
    if df[column].name == "rownames":
        df.drop(column, axis=1, inplace=True)

# Displays columns names
print("Available columns:")
print(df.columns.tolist())


# Ask user to select their vairables
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

# Creating the scatterplot
fig, ax = plt.subplots(figsize=(8,6))

ax.scatter(data[x_col], data[y_col], alpha=0.6, edgecolor="k", linewidth=0.3)

ax.set_xlabel(x_col)
ax.set_ylabel(y_col)
ax.set_title(f"{y_col} vs. {x_col}")
ax.grid(alpha=0.3)

fig.tight_layout()


# Prompts user to save the scatterplot if they want
save_scatter = input("Do you want to save the scatter plot? (y/n): ").strip().lower()

# Changed it to automatically save it as the filename f"{df[x_col]}_vs_{y_col}.png"
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
ax.plot(x_line, y_line, color="crimson", linewidth=2,
        label=f"OLS Line (R^2 = {model.rsquared:.3f})")

ax.legend()
ax.set_title(f"{x_col} vs. {y_col} with OLS regression line")

# Ask the user to save scatterplot
save_ols = input("Do you want to save the OLS plot? (y/n): ").strip().lower()

# Changed the input file name to f"{df[x_col]}_vs_{y_col}.png"
if save_ols in ["y", "yes"]:
    ols_filename = f"{x_col}_vs_{y_col}.png"
    fig.savefig(ols_filename + ".png", dpi = 300)
    print("OLS plot saved")

plt.show()
