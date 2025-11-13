import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cryptos_unidas.csv")

def grafico(cripto,desde=None):
    datos = df[df["Name"] == cripto]
    datos["Date"] = pd.to_datetime(datos["Date"])
    datos = datos.sort_values("Date")
    datos["Close"] = pd.to_numeric(datos["Close"])
    if desde:
        desdedatetime= pd.to_datetime(desde)
        datos = datos[datos["Date"] >= desdedatetime]
    plt.figure(figsize=(10, 5))
    plt.plot(datos["Date"], datos["Close"], linewidth=2,color ="red")
    plt.title(f"Precio histórico - {cripto}", fontsize=12)
    plt.xlabel("Fecha", fontsize=12)
    plt.ylabel("Precio (USD)", fontsize=12)
    #plt.savefig(f"Marketcap_{cripto}.png")
    plt.show()



grafico("Bitcoin")


