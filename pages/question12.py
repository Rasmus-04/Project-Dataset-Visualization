import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd
 
#df = pd.read_pickle("data/preparedData/df_q12.pkl")

dash.register_page(
    __name__,
    path="/question-12",
    name="Question 12"
)

layout = html.Div([
    html.H2("Question 12: Do any platforms seem to specialize in a particular genre?"),

    dcc.Graph(id="q12-graph")
])


@dash.callback(
    Output("q12-graph", "figure")
)
def update_q12_figure():
    fig = 0
    return fig