import plotly.offline as pyo
import plotly_express as pye
import pandas as pd

df = pd.read_csv("datos.csv")

dato_hist = pye.histogram(df.Mexico, x="Mexico")
dato_hist.show()

# pyo.plot([{
#     'x': df.Mexico,
#     'y': df.USA
# }])
