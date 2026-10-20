import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

dash.register_page(
    __name__,
    path="/question-5",
    name="Question 5"
)

layout = html.Div([
    html.H2("Question 5: Which regions prefer which genre the most?")
])