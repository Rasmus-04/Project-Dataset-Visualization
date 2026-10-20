import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

dash.register_page(
    __name__,
    path="/question-3",
    name="Question 3"
)
layout = html.Div([
    html.H2("Question 3: How do video game sales vary per release year in each region?")
])