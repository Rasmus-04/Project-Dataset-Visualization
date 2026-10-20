import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

dash.register_page(
    __name__,
    path="/question-8",
    name="Question 8"
)

layout = html.Div([
    html.H2("Question 8: Which publishers have consistent success and which publishers are hit or miss with games?")
])