##########
# Convert to JSON # Madison J Lowenstein #
# 9/29/26 # mlowenstein@usf.edu
###########

import pandas as pd


df = pd.read_parquet("Maternal_Health_Risk.parquet")

df.to_json("Maternal Health Risk Data Set.json", orient="records", indent=2)

