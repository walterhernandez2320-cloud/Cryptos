import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cryptos_unidas.csv")

def torta(variable):
    datos = df[["Name", variable]]
    datos[variable] = pd.to_numeric(datos[variable])
    agrupado = datos.groupby("Name")[variable].sum()
    total = agrupado.sum()
    porcentajes = (agrupado / total) * 100

    plt.figure(figsize=(10, 10))
    plt.pie(agrupado, labels=porcentajes.index, autopct=lambda p: f"{p:.1f}%", startangle=90)
    plt.title(f"Aporte de cada criptomoneda — {variable}", fontsize=12)
    plt.tight_layout()
    plt.savefig(f"Grafico de torta para {variable}")
    plt.show()

torta("Marketcap")