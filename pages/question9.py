import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

dash.register_page(
    __name__,
    path="/question-9",
    name="Question 9"
)

layout = html.Div([
    html.H2("Question 9: Which region purchases the most video games?")
])