import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

dash.register_page(
    __name__,
    path="/question-4",
    name="Question 4"
)

layout = html.Div([
    html.H2("Question 4: Which platforms for playing video games have been the most popular each release year?")
])