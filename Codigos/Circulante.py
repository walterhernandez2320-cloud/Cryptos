import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv("cryptos_unidas.csv")
df.set_index('Date')
#print(df.head())
moneda = df[df["Name"] == "Bitcoin"] 
valor = moneda["Marketcap"]
valor = pd.to_numeric(valor)
precio = moneda["Close"]
precio = pd.to_numeric(precio)
circulante = valor / precio 
print(circulante)
circulante.plot(style='o-')
plt.show()