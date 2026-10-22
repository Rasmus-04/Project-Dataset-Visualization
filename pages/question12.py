import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd
 
df = pd.read_pickle("data/preparedData/df_q12.pkl")
 
dash.register_page(
    __name__,
    path="/question-12",
    name="Question 12"
)

platforms_by_sales = df["platform"].unique().tolist()
 
# Metric: (kolumn, färgskala-titel, textformat)
METRICS = {
    "genre_share": ("Share of platform's sales (%)", ".0f"),
    "specialization_index": ("Specialization index (1 = market average)", ".2f"),
    "total_sales": ("Sales (millions)", ".1f"),
}
 
layout = html.Div([
    html.H2("Question 12: Do any platforms seem to specialize in a particular genre?"),
 
    html.Div([
        html.Div([
            html.Label("Number of platforms (ranked by total sales)"),
            dcc.Slider(
                id="q12-top-n",
                min=5,
                max=min(40, len(platforms_by_sales)),
                step=1,
                value=15,
                marks={n: str(n) for n in [5, 10, 15, 20, 30, 40] if n <= len(platforms_by_sales)},
                tooltip={"placement": "bottom", "always_visible": False},
            ),
        ], style={"flex": "2", "marginRight": "30px"}),
 
        html.Div([
            html.Label("Show"),
            dcc.RadioItems(
                id="q12-metric",
                options=[
                    {"label": " Genre share of platform (%)", "value": "genre_share"},
                    {"label": " Specialization index", "value": "specialization_index"},
                    {"label": " Absolute sales (millions)", "value": "total_sales"},
                ],
                value="genre_share",
            ),
        ], style={"flex": "1"}),
    ], style={"display": "flex", "marginBottom": "20px"}),
 
    dcc.Graph(id="q12-graph"),
])
 
 
@dash.callback(
    Output("q12-graph", "figure"),
    Input("q12-top-n", "value"),
    Input("q12-metric", "value"),
)
def update_q12_figure(top_n, metric):
    selected_platforms = platforms_by_sales[:top_n]
    sel = df[df["platform"].isin(selected_platforms)]
 
    # Plattformar som rader, genrer som kolumner. Saknad kombination = ingen registrerad försäljning (tom ruta).
    matrix = sel.pivot(index="platform", columns="genre", values=metric).reindex(selected_platforms)
 
    color_label, text_format = METRICS[metric]
 
    if metric == "specialization_index":
        color_scale = "RdBu_r"
        midpoint = 1  # Centrerar färgskalan på 1 så att över/under genomsnittet syns direkt
    else:
        color_scale = "Blues"
        midpoint = None  # Ingen mittpunkt, vanlig skala

    fig = px.imshow(
        matrix,
        text_auto=text_format,
        aspect="auto",
        color_continuous_scale=color_scale,
        color_continuous_midpoint=midpoint,
        labels={"x": "Genre", "y": "Platform", "color": color_label}
    )

    fig.update_xaxes(side="top")
    fig.update_layout(height=max(450, 32 * top_n + 150))

    fig.update_layout(
        title={"text": "Platform and genre: where do platforms specialize?", "y": 0.98},
        height=max(450, 32 * top_n + 190),
)
    
    return fig