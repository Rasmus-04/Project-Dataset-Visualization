import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

dash.register_page(
    __name__,
    path="/question-7",
    name="Question 7"
)

layout = html.Div([
    html.H2("Question 7: Which genres have been more or less popular with the passing of time?")
])