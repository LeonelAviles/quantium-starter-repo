import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

data_frame = pd.read_csv("DATA_FORMATTED")
data_frame = data_frame.sort_values(by=['Date'])

fig = px.line(data_frame, x="Date", y="Sales")

app = Dash()

app.layout = [
    html.Div(children=[
        html.H1(children="Impact of Pink Morsel's Price Increase on Sales"),
    ]),
    dcc.Graph(id="line-data", figure=fig),
]

if __name__ == '__main__':
    app.run()