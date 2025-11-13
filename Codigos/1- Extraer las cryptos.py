
import pandas as pd

df = pd.read_csv("cryptos_unidas.csv")
lista_criptos = df["Name"].unique()
lista_criptos = sorted(lista_criptos)
dataframe= pd.DataFrame(lista_criptos, columns=["CRIPTOS PRESENTES"])
dataframe.to_csv("criptos_presentes.csv", index=False)


