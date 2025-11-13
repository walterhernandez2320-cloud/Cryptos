import pandas as pd
import plotly.express as px

df = pd.read_csv("cryptos_unidas.csv")
df["Marketcap"] = pd.to_numeric(df["Marketcap"], errors="coerce")
df["Volume"] = pd.to_numeric(df["Volume"], errors="coerce")
df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
def tortainteractivo(columna: str):
    tabla = df.groupby("Name")[columna].sum().reset_index()

    fig = px.pie(
        tabla,
        names="Name",
        values=columna,
        title=f"Distribución total de {columna} por criptomoneda",

    )

    fig.show()
    return

tortainteractivo("Marketcap")