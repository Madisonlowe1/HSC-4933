#################################
# Lab 10/ survival Analysis Lab #
### Madison Lowenstein ###
### mlowenstein@usf.edu ###
### 11/1/2026 ###
# Kaplan-Meier log-rank test #
#################################

import matplotlib.pyplot as plt
import pandas as pd
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test


csv_file_path = "km_logrank_readmission.csv"

# Specify columns
time_column = "time_days"
event_column = "readmitted"
group_column = "treatment_group"

# load dataset
df = pd.read_csv(csv_file_path)

kmf = KaplanMeierFitter()
fig, ax = plt.subplots(figsize=(10, 6))

logrank_result = None

if group_column and group_column in df.columns:
    for group_name, group_df in df.groupby(group_column):
        kmf.fit(
            durations=group_df[time_column],
            event_observed = group_df[event_column],
            label=f"Group {group_name}",
        )
        kmf.plot_survival_function(ax=ax, show_censors=True)

    group_std = df[df[group_column] == "Standard care"]
    group_tel = df[df[group_column] == "Telehealth follow-up"]

    if len(group_std) > 0 and len(group_tel) > 0:
        logrank_result = logrank_test(
            durations_A=group_std[time_column],
            durations_B = group_tel[time_column],
            event_A=group_std[event_column],
            event_B = group_tel[event_column],
        )
        print("Log-rank test: Standard care vs. Telehealth follow-up")
        print(f" Test statistic (chi-square) = {logrank_result.test_statistic:.4f}")
        print(f" p-value = {logrank_result.p_value:.4g}")

if logrank_result is not None:
    p = logrank_result.p_value
    p_text = "p < .001" if p < .001 else f"p= {p:.3f}"
    ax.text(
        .97, .97,
        f"log-rank test\n{p_text}",
        ha="right", va="top",
        fontsize=11,
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.8),
    )

plt.title("Kaplan-Meier Readmission-Free Survival (180 Days)", fontsize=14)
plt.xlabel("Time Post Discharge (Days)", fontsize=12)
plt.ylabel("Survival Probability", fontsize=12)
plt.ylim(0, 1.05)
plt.grid(True, linestyle="--", alpha=.6)
plt.legend(loc="lower left")
plt.tight_layout()

plt.savefig("km_logrank_readmission.png")

plt.show()


