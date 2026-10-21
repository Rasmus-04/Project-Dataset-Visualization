import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd
 
#df = pd.read_pickle("data/preparedData/df_q13.pkl")

dash.register_page(
    __name__,
    path="/question-13",
    name="Question 13"
)

layout = html.Div([
    html.H2("Question 13: What titles are popular in one region but flop in another?"),

    dcc.Graph(id="q13-graph")
])


@dash.callback(
    Output("q13-graph", "figure")
)
def update_q13_figure():
    fig = 0
    return fig