##########
# Convert to xlsx # Madison J Lowenstein #
# 9/29/26 # mlowenstein@usf.edu
###########

import pandas as pd

df = pd.read_csv("Maternal Health Risk Data Set.csv")

df = df.drop(columns=["Unnamed: 0"], errors="ignore")
df.to_excel("Maternal Health Risk Data Set.xlsx", engine='openpyxl', index=False)
