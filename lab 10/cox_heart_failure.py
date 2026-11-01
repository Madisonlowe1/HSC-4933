#################################
# Lab 10/ survival Analysis Lab #
### Madison Lowenstein ###
### mlowenstein@usf.edu ###
### 11/1/2026 ###
# Cox proportional hazards test #
#################################

import matplotlib.pyplot as plt
import pandas as pd
from lifelines import CoxPHFitter

csv_file_path = "cox_ph_heart_failure_survival.csv"

time_column = "time_months"
event_column = "death"
numeric_covariates = ["age", "bmi", "systolic_bp", "ejection_fraction"]
binary_covariates = ["sex", "diabetes", "smoker", "chronic_kidney_disease", "beta_blocker"]
categorical_covariates = ["nyha_class"]

df = pd.read_csv(csv_file_path)

df["sex"] = df["sex"].astype(str).str.strip().isin(["Male", "1", "true", "yes"]).astype(int)

for col in binary_covariates:
    if col != "sex":
        df[col] = df[col].astype(str).str.strip().str.lower().isin(["true", "1", "yes", "1.0"]).astype(int)

model_df = df[[time_column, event_column] + numeric_covariates + categorical_covariates + binary_covariates]
model_df = pd.get_dummies(model_df, columns=categorical_covariates, drop_first=True, dtype=int)
model_df = model_df.dropna()

cph = CoxPHFitter()
cph.fit(model_df, duration_col=time_column, event_col=event_column)

cph.print_summary(decimals=3)
print(f"\nConcordance index: {cph.concordance_index_:.3f}")

print("\n--- Proportional hazards assumption check ---")
cph.check_assumptions(model_df, p_value_threshold=0.05, show_plots=False)

fig, ax = plt.subplots(figsize=(8, 5))
cph.plot(hazard_ratios=True, ax=ax)
ax.axvline(1, color="gray", linestyle="--")
ax.set_title("Cox PH Model: Hazard Ratios (95% CI)", fontsize=14)
plt.tight_layout()
plt.savefig("cox_heart_failure.png")

plt.show()

