##############################################
### Lab # 7 # Linear Regression Lab ##########
########### birthwt data######################
########### for fig_1 and fig_2 ############
# Madison Lowenstein # mlowenstein@usf.edu ###
##############################################

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("birthwt.csv")

print(df.shape, df.dtypes, df.isnull().sum(), df.nunique(), sep="\n")

print("duplicates:", df.duplicated().sum())

df.columns = df.columns.str.lower().str.replace(" ", "_")

X_COL = "lwt"
Y_COL = "bwt"

data =df[[X_COL, Y_COL]].dropna()

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(data[X_COL], data[Y_COL], alpha=0.6, edgecolor="k", linewidth=0.3)
ax.set_xlabel(X_COL)
ax.set_ylabel(Y_COL)
ax.set_title(f"{Y_COL} vs {X_COL} (n = {len(data)})")
ax.grid(alpha=0.3)
fig.tight_layout()

scatter_file =  "fig_1.png"
fig.savefig(scatter_file, dpi=300)
print(f"saved scatterplot to {scatter_file}")

X = sm.add_constant(data[X_COL])
model = sm.OLS(data[Y_COL], X).fit()

print("OLS Regression Summary:")
print(model.summary())

x_line = np.linspace(data[X_COL].min(), data[X_COL].max(), 100)
y_line = model.params["const"] + model.params[X_COL] * x_line
ax.plot(x_line, y_line, color="crimson", linewidth=2, label=f"OLS line (R² = {model.rsquared:.3f}) ")
ax.set_title(f"{Y_COL} vs {X_COL} with OLS line (n = {len(data)})")
ax.legend()

ols_file = f"fig_2.png"
fig.savefig(ols_file, dpi=300)
print(f"saved OLS plot to {ols_file}")

plt.show()
