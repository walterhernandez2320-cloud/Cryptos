import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cryptos_unidas.csv")

def grafico(cripto):
    data = df[df["Name"] == cripto]
    data["Date"] = pd.to_datetime(data["Date"])
    data = data.sort_values("Date")
    data["Marketcap"] = pd.to_numeric(data["Marketcap"])
    #Usando matplotlib
    plt.figure(figsize=(10, 5))
    plt.plot(data["Date"], data["Marketcap"], linewidth=2,color ="red")
    plt.title(f"Marketcap histórico - {cripto}", fontsize=12)
    plt.xlabel("Fecha", fontsize=12)
    plt.ylabel("Marketcap (USD)", fontsize=12)
    plt.savefig(f"Marketcap_{cripto}.png")
    plt.show()


grafico("Ethereum")
