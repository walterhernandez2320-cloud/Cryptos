import pandas as pd
import plotly.express as px

def grafint(cripto:str,desde=None):
    df = pd.read_csv("cryptos_unidas.csv")
    datos = df[df["Name"] == cripto].sort_values("Date")
    datos["Date"] = pd.to_datetime(df["Date"])
    datos["Marketcap"] = pd.to_numeric(df["Marketcap"])
    if desde:
        desdedatetime= pd.to_datetime(desde)
        datos = datos[datos["Date"] >= desdedatetime]
    fig = px.line(
        datos,
        x="Date",
        y="Marketcap",
        title=f"Marketcap histórico — {cripto}",
        labels={"Date": "Fecha", "Marketcap": "Marketcap (USD)"})
    fig.show()
    return


grafint("Bitcoin",desde="2020/7/2")

        
