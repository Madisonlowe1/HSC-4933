##########################
# Lab 9: Logistic and Count-variable regression #
# Madison Lowenstein / mlowenstein@usf.edu #
######### 10/23/26 ########

import pandas as pd
import numpy as np

import statsmodels.formula.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools import add_constant
from sklearn.metrics import confusion_matrix, accuracy_score

file_path = input("Enter file path: ").strip()
df = pd.read_csv(file_path)

df.columns = df.columns.str.lower().str.replace(" ", "_")

print("\nAvailable Column Names:")
for col in df.columns:
    print(f" - {col}")

reg_type = input("\nSelect Regression Type (l for Logistic, p for Poisson): ").strip()
response_var = input("Enter the response variable: ").strip()
predictors_input = input("Enter predictor variables separated by a comma: ").strip()
predictors = [p.strip() for p in predictors_input.split(",")]

df = df.dropna(subset=[response_var] + predictors)

formula = f"{response_var} ~ " + " + ".join(predictors)

output_text = ""

if reg_type == "l":
    model = smf.logit(formula, data=df).fit()
    summary_str = str(model.summary())

    preds = (model.predict(df) >= 0.5).astype(int)
    acc = accuracy_score(df[response_var], preds)
    cm = confusion_matrix(df[response_var], preds)

    output_text = f"=== LOGISTIC REGRESSION OUTPUT ===\n\n{summary_str}\n\nModel Accuracy: {acc:.4f}\n\nConfusion Matrix:\n{str(cm)}"

else:
    model = smf.poisson(formula, data=df).fit()
    summary_str = str(model.summary())

    X_vif = add_constant(df[predictors])
    vif_df = pd.DataFrame()
    vif_df["Variable"] = X_vif.columns
    vif_df["VIF"] = [variance_inflation_factor(X_vif.values, i) for i in range(X_vif.shape[1])]

    output_text = f"=== COUNT-VARIABLE REGRESSION OUTPUT ===\n\n{summary_str}\n\nVIF Output:\n{vif_df.to_string(index=False)}"

print("\n + Output Text:")

save_choice = input("\nWould you like to save the output to file (y/n): ").strip().lower()
if save_choice == "y":
    filename = input("Enter file path: ").strip()
    with open(filename, "w") as f:
        f.write(output_text)
    print(f"Output saved to '{filename}'.")