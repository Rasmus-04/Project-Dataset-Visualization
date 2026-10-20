import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

dash.register_page(
    __name__,
    path="/question-10",
    name="Question 10"
)

layout = html.Div([
    html.H2("Question 10: Which titles sold the most worldwide?")
])