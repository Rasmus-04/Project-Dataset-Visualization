import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

dash.register_page(
    __name__,
    path="/question-6",
    name="Question 6"
)

layout = html.Div([
    html.H2("Question 6: What are the top three genres per region?")
])