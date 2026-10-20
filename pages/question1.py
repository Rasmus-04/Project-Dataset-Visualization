import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

dash.register_page(
    __name__,
    path="/question-1",
    name="Question 1"
)

layout = html.Div([
    html.H2("Question 1: Which regions prefer which platform the most for playing video games?")
])