import pandas as pd 
df = pd.read_csv("cryptos_unidas.csv")

def rango(cripto:str):
    nombre = df[df["Name"] == cripto]
    fechas = nombre["Date"]
    fechas = pd.to_datetime(fechas)
    antigua = fechas.min()
    nueva = fechas.max()
    print(antigua,nueva)
    return

rango("Dogecoin")
rango("Bitcoin")
rango("Ethereum")


