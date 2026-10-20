import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

dash.register_page(
    __name__,
    path="/question-12",
    name="Question 12"
)

layout = html.Div([
    html.H2("Question 12: Do any platforms seem to specialize in a particular genre?")
])