import plotly.offline as pyo
import plotly_express as pyx
import plotly.graph_objects as go
import pandas as pd
import plotly.figure_factory as ff
data = pd.read_csv("sample_semanai.csv")

dato_hist = pyx.histogram(data, x="Clave platillo")


data_ham = data[data["Tipo de grupo"] == "Alimentos"]
ham_hist = pyx.histogram(data_ham, x="Clave platillo")
# ham_hist.show()

data_bebidas = data[data["Tipo de grupo"] == "Bebidas"]
bebidas_hist = pyx.histogram(data_bebidas, x="Clave platillo")
bebidas_hist.show()

fig = ff.create_dendrogram()
