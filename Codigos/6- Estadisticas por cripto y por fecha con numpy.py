import pandas as pd
import numpy as np

df = pd.read_csv("cryptos_unidas.csv")
df["Close"] = pd.to_numeric(df["Close"])
df["Marketcap"] = pd.to_numeric(df["Marketcap"])
df["Volume"] = pd.to_numeric(df["Volume"])

def estadisticas(cripto: str,desde=None):
    datos = df[df["Name"]]== cripto
    estadisticas = {"Variable (en USD)": ["Close", "Marketcap", "Volume"],"Media": [np.mean(datos["Close"]), np.mean(datos["Marketcap"]), np.mean(datos["Volume"])],"Mediana": [np.median(datos["Close"]), np.median(datos["Marketcap"]), np.median(datos["Volume"])],"Desvío estándar": [np.std(datos["Close"]), np.std(datos["Marketcap"]), np.std(datos["Volume"])]}
    tabla = pd.DataFrame(estadisticas)
    tabla = tabla.round(2)
    nombrecsv = f"estadisticas_{cripto}.csv"
    tabla.to_csv(nombrecsv, index=False)
    return tabla


