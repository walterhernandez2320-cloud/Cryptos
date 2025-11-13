import pandas as pd

df = pd.read_csv("cryptos_unidas.csv")
variables = df.columns
dataframe_variables = pd.DataFrame(variables, columns=["Variables presentes en el CSV"])
dataframe_variables.to_csv("variables_presentes.csv", index=False)
