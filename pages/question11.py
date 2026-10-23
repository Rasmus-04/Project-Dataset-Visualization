import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import numpy as np
import pandas as pd
 
df = pd.read_pickle("data/preparedData/df_q11.pkl")

 
dash.register_page(
    __name__,
    path="/question-11",
    name="Question 11"
)

 
MIN_YEAR = int(df["release_year"].min())
MAX_YEAR = int(df["release_year"].max())
 
layout = html.Div([
    html.H2("Question 11: Which release year had the highest sales, and is the industry growing over time?"),

    html.Div(
        [
            html.Label("Release years"),
            dcc.RangeSlider(
                id="q11-years",
                min=MIN_YEAR,
                max=MAX_YEAR,
                step=1,
                value=[MIN_YEAR, MAX_YEAR],
                marks={y: str(y) for y in range(MIN_YEAR - MIN_YEAR % 5, MAX_YEAR + 1, 5)},
                tooltip={"placement": "bottom", "always_visible": False},
            ),
        ], style={"marginBottom": "30px"}
    ),
 
    dcc.Graph(id="q11-graph"),
])
 
 
@dash.callback(
    Output("q11-graph", "figure"),
    Input("q11-years", "value")
)
def update_q11(year_range):
    start, end = year_range
    sel = df[(df["release_year"] >= start) & (df["release_year"] <= end)].copy()
    
    # Toppår och linjär trend inom det valda intervallet
    peak = sel.loc[sel["total_sales"].idxmax()]

 
    # Toppåret får en egen färg
    sel["highlight"] = np.where(sel["release_year"] == peak["release_year"], "Peak year", "Other years")

    fig = px.bar(
        sel,
        x="release_year",
        y="total_sales",
        color="highlight",
        color_discrete_map={"Peak year": "#EF553B", "Other years": "#636EFA"},
        labels={
            "release_year": "Release year",
            "total_sales": "Worldwide sales (millions)",
            "highlight": "",
        },
        title="Worldwide sales per release year",)

    return fig