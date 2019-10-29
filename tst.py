import plotly.offline as pyo
import plotly_express as pyx
import plotly.graph_objects as go
import pandas as pd

data = pd.read_csv("sample_semanai.csv")

dato_hist = pyx.histogram(data, x="Clave platillo")
# dato_hist.show()

stacked_bar = go.Figure(data=[
    go.Bar(name="HAMBURGUESAS", x=data["Día"], y=data["Grupo"]),
    go.Bar(name="ENTRADAS", x=data["Día"], y=data["Grupo"]),
    go.Bar(name="BEBIDAS SIN ALCOHOL", x=data["Día"], y=data["Grupo"]),
    go.Bar(name="BEBIDAS CON ALCOHOL", x=data["Día"], y=data["Grupo"]),
    go.Bar(name="POSTRES", x=data["Día"], y=data["Grupo"]),
    go.Bar(name="CLÁSICOS", x=data["Día"], y=data["Grupo"]),
    go.Bar(name="PAPAS, PAPAS Y MÁS PAPAS", x=data["Día"], y=data["Grupo"]),
    go.Bar(name="BÁSICOS", x=data["Día"], y=data["Grupo"]),
    go.Bar(name="PASTAS", x=data["Día"], y=data["Grupo"]),
    go.Bar(name="EXTRAS COCINA", x=data["Día"], y=data["Grupo"])
])

stacked_bar.update_layout(barmode='stack')
stacked_bar.show()
