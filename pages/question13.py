import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

dash.register_page(
    __name__,
    path="/question-13",
    name="Question 13"
)

layout = html.Div([
    html.H2("Question 13: What titles are popular in one region but flop in another?")
])