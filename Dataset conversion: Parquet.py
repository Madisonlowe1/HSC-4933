##########
# Convert to Parquet # Madison J Lowenstein #
# 9/29/26 # mlowenstein@usf.edu
###########

import pandas as pd

df = pd.read_csv("Maternal Health Risk Data Set.csv")

df = df.drop(columns=['Unnamed: 0'], errors='ignore')
df.to_parquet("Maternal_Health_Risk.parquet", engine='pyarrow', index=False)



