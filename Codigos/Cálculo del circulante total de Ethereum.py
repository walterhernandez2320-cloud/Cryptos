import pandas as pd

df = pd.read_csv("cryptos_unidas.csv")

eth = df[df["Name"] == "Ethereum"]
eth["Date"] = pd.to_datetime(eth["Date"])
eth = eth.sort_values("Date")

ultimo = eth.iloc[-1] # aca se buscan los datos del ultimo dia del CSV que tiene informacion de Ethereum
circulante = ultimo["Marketcap"] / ultimo["Close"]

print("Fecha:", ultimo["Date"])
print("Marketcap:", ultimo["Marketcap"])
print("Circulante total:", circulante)
