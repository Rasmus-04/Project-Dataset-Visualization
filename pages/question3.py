import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Laddar in den förberrada datframen
df = pd.read_pickle("data/preparedData/df_q3.pkl")

regions = {
    "North America": "na_sales",
    "Japan": "jp_sales",
    "Europe and Africa": "pal_sales",
    "Other": "other_sales"
}

dash.register_page(
    __name__,
    path="/question-3",
    name="Question 3"
)
layout = html.Div([
    html.H2("Question 3: How do video game sales vary per release year in each region?"),

    html.Label('Regions:'),
    dcc.Dropdown(id='hist_multi_region_selector',
    multi=True, 
    value=["na_sales", "jp_sales", "pal_sales", "other_sales"],
    placeholder='Select one or more years',
    options=[{"label": region, "value": column} for region, column in regions.items()]
    ),

    dcc.Graph(id="q3-graph")
])

@dash.callback(
    Output("q3-graph", "figure"),
    Input("hist_multi_region_selector", "value")
)
def update_q3_graph(selected_regions):
    # Gör om de regionala kolumnerna till rader så att varje releaseår får en rad per region
    df_q3 = df.melt(
        id_vars="release_year", # Behåller release_year som en kolumn
        value_vars=selected_regions, # Väljer vilka regioner som ska vara med i grafen
        var_name="region", # Skapar en kolumn som innehåller regionernas kolumnnamn
        value_name="sales" # Skapar en kolumn som innehåller försäljningen
    )

    # Byter ut kolumnnamnen mot mer läsbara regionnamn, exempelvis na_sales till North America
    df_q3["region"] = df_q3["region"].map({column: region for region, column in regions.items()})

    fig = px.line(
        df_q3,
        x="release_year",
        y="sales",
        color="region",
        markers=True,
        title="Video Game Sales per Release Year and Region",
        labels={
            "release_year": "Release Year",
            "sales": "Total Sales (millions)",
            "region": "Region"
        }
    )

    fig.update_layout(
        height=600
    )

    return fig