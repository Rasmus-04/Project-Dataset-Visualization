import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_pickle("data/preparedData/df_q8.pkl")

dash.register_page(
    __name__,
    path="/question-8",
    name="Question 8"
)

max_games = int(df["games_with_sales"].max())

layout = html.Div([
    html.H2("Question 8: Which publishers have consistent success and which publishers are hit or miss with games?"),
    html.P("Size is defind by the publishers total sales"),
    html.Div([
        html.Label("Minimum number of games with recorded sales per publisher"),
        dcc.Slider(
            id="q8-min-games",
            min=2,
            max=min(max_games, 100),
            step=1,
            value=10,
            marks={n: str(n) for n in [2, 10, 25, 50, 75, 100] if n <= max_games},
            tooltip={"placement": "bottom", "always_visible": False},
        ),
    ], style={"marginBottom": "30px", "width": "70%"}),

    dcc.Graph(id="q8-graph", style={"height": "700px"})
])


@dash.callback(
    Output("q8-graph", "figure"),
    Input("q8-min-games", "value"),
)
def update_q8_figure(min_games):
    # Coefficient of variation(CV)
    # CV = variationskoefficienten (std_sales / mean_sales)

    # Publishers med för få spel ger opålitliga mått, och std saknas vid ett enda spel
    filtered = df[(df["games_with_sales"] >= min_games) & df["cv"].notna() & (df["mean_sales"] > 0)]

    # Delar upp publishers vid medianen av CV bland de som visas
    cv_threshold = filtered["cv"].median()
    filtered["profile"] = filtered["cv"].apply(lambda value: "Consistent" if value <= cv_threshold else "Hit or miss")

    fig = px.scatter(
        filtered,
        x="mean_sales",
        y="cv",
        size="total_sales",
        color="profile",
        hover_name="publisher",
        hover_data={
            "games_with_sales": True,
            "total_sales": ":.1f",
            "mean_sales": ":.2f",
            "median_sales": ":.2f",
            "max_sales": ":.2f",
            "cv": ":.2f"
        },
        log_x=True,
        size_max=45,
        category_orders={"profile": ["Consistent", "Hit or miss"]},
        labels={
            "mean_sales": "Average sales per game (millions, log scale)",
            "cv": "Variation in sales (std / mean)",
            "profile": "Profile",
            "total_sales": "Total sales (millions)",
            "games_with_sales": "Games with sales",
            "median_sales": "Median sales",
            "max_sales": "Best-selling game",
        },
        title="Publisher consistency: average sales vs. variation in sales",
    )
    fig.add_hline(
        y=cv_threshold,
        line_dash="dash",
        line_color="gray",
        annotation_text="Median variation",
        annotation_position="top left",
    )
    fig.update_layout(legend_title_text="Profile")
    return fig