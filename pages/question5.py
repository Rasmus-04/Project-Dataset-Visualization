import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_pickle("data/preparedData/df_q5.pkl")

dash.register_page(
    __name__,
    path="/question-5",
    name="Question 5"
)

layout = html.Div([
    html.H2("Question 5: Which regions prefer which genre the most?"),
    dcc.Graph(id="q5-graph")
])


@dash.callback(
    Output("q5-graph", "figure")
)
def update_q5_heat_graph():

    # Hämtar alla kolumner utom genre så att vi bara får med försäljningsdatan
    sales_columns = [column for column in df.columns if column != "genre"]

    # Gör genre till index och hämtar försäljningen för varje region
    genre_sales = df.set_index("genre")[sales_columns]

    # Sorterar genrerna efter total försäljning, från högst till lägst
    genre_sales = genre_sales.loc[genre_sales.sum(axis=1).sort_values(ascending=False).index]

    genre_sales = genre_sales.rename(columns={
        "na_sales": "North America",
        "jp_sales": "Japan",
        "pal_sales": "European & African",
        "other_sales": "Other"
    })

    # Räknar ut hur stor procentandel varje genre står för av regionens totala försäljning
    genre_share = (genre_sales.div(genre_sales.sum(axis=0), axis=1) * 100)

    fig = px.imshow(
        genre_share,
        x=genre_share.columns,
        y=genre_share.index,
        aspect="auto",
        color_continuous_scale="Viridis",
        text_auto=".1f",
        labels={
            "x": "Region",
            "y": "Genre",
            "color": "Share of regional sales (%)"
        },
        title="Relative Genre Popularity by Region"
    )

    fig.update_layout(
        height=700,
        xaxis_title="Region",
        yaxis_title="Genre",
        coloraxis_colorbar_title="Sales share (%)"
    )

    return fig
