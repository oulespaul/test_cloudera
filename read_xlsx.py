import pandas as pd

df = pd.read_excel("out_load.xlsx", engine="openpyxl")

print(df)
