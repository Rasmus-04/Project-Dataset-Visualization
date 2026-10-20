import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

dash.register_page(
    __name__,
    path="/question-11",
    name="Question 11"
)

layout = html.Div([
    html.H2("Question 11: Which release year had the highest sales, and is the industry growing over time?")
])