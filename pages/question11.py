import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd
 
#df = pd.read_pickle("data/preparedData/df_q11.pkl")

dash.register_page(
    __name__,
    path="/question-11",
    name="Question 11"
)

layout = html.Div([
    html.H2("Question 11: Which release year had the highest sales, and is the industry growing over time?"),

    dcc.Graph(id="q11-graph")
])


@dash.callback(
    Output("q11-graph", "figure")
)
def update_q11_figure():
    fig = 0
    return fig