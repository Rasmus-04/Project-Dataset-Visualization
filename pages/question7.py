import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd
 
df = pd.read_pickle("data/preparedData/df_q7.pkl")
 
dash.register_page(
    __name__,
    path="/question-7",
    name="Question 7"
)
 
# Genrer sorterade efter total försäljning (högst först), används för dropdown och standardval
genres_by_sales = df.groupby("genre")["total_sales"].sum().sort_values(ascending=False).index.tolist()
DEFAULT_GENRES = genres_by_sales[:5]
 
# Försäljning per år över ALLA genrer används för att räkna ut andelar i %
yearly_total = df.groupby("release_year")["total_sales"].transform("sum")
df = df.assign(share=df["total_sales"] / yearly_total * 100)
 
layout = html.Div([
    html.H2("Question 7: Which genres have been more or less popular with the passing of time?"),
 
    html.Div([
        html.Div([
            html.Label("Genres"),
            dcc.Dropdown(
                id="q7-genres",
                options=[{"label": g, "value": g} for g in genres_by_sales],
                value=DEFAULT_GENRES,
                multi=True,
            ),
        ], style={"flex": "3", "marginRight": "20px"}),
 
        html.Div([
            html.Label("Show"),
            dcc.RadioItems(
                id="q7-metric",
                options=[
                    {"label": " Worldwide sales (millions)", "value": "total_sales"},
                    {"label": " Share of yearly sales (%)", "value": "share"},
                ],
                value="total_sales",
            ),
        ], style={"flex": "1"}),
    ], style={"display": "flex", "marginBottom": "20px"}),
 
    dcc.Graph(id="q7-graph")
])
 
 
@dash.callback(
    Output("q7-graph", "figure"),
    Input("q7-genres", "value"),
    Input("q7-metric", "value"),
)
def update_q7_figure(selected_genres, metric):
    filtered = df[df["genre"].isin(selected_genres)].sort_values("release_year")
 
    is_share = metric == "share"
    y_label = "Share of yearly sales (%)" if is_share else "Worldwide sales (millions)"
 
    fig = px.line(
        filtered,
        x="release_year",
        y=metric,
        color="genre",
        markers=True,
        labels={"release_year": "Release year", metric: y_label, "genre": "Genre"},
        title="Genre popularity over time",
    )
    fig.update_layout(hovermode="x unified", legend_title_text="Genre")
    return fig