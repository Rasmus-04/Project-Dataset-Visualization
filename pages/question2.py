import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Laddar in den förberrada datframen
df = pd.read_pickle("data/preparedData/df_q2.pkl")

dash.register_page(
    __name__,
    path="/question-2",
    name="Question 2"
)


layout = html.Div([
    html.H2("Question 2: What is the most popular platform for playing video games?"),

    html.Div([
        html.Label("Number of platforms"),
        dcc.Slider(
            id="row-slider",
            min=10,
            max=20,
            step=5,
            marks={10: "10", 15: "15", 20: "20"},
            value=15
        )
    ], style={"maxWidth": 600}),

    dcc.Graph(id="q2-graph")
])


@dash.callback(
    Output("q2-graph", "figure"),
    Input("row-slider", "value")
)
def update_q2_graph(nr_of_rows):

    top_platforms_df = (
        df
        .nlargest(nr_of_rows, "total_sales")  # hämtar de {the nr_of_rows} största värderna i den valde regionen 
        .sort_values("total_sales", ascending=True) # Sorterar efter storlek
    )

    fig = px.bar(
    top_platforms_df,
    x="total_sales",
    y="platform",
    orientation="h",
    title="Top Gaming Platforms by Global Sales",
    labels={"total_sales": "Total Sales (millions)", "platform": "Platform"}
    )

    fig.update_layout(
        template="plotly_white",
        yaxis={"categoryorder": "total ascending"},
        height=600
    )

    return fig