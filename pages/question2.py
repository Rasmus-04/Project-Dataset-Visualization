import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

dash.register_page(
    __name__,
    path="/question-2",
    name="Question 2"
)



layout = html.Div([
    html.H2("Question 2: What is the most popular platform for playing video games?"),
])