import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_pickle("data/preparedData/df_q6.pkl")

REGION_NAMES = {
    "na_sales": "North America",
    "jp_sales": "Japan",
    "pal_sales": "Europe and Africa",
    "other_sales": "Other"
}

dash.register_page(
    __name__,
    path="/question-6",
    name="Question 6"
)

layout = html.Div([
    html.H2("Question 6: What are the top three genres per region?"),

    dcc.Graph(id="q6-graph")
])


@dash.callback(
    Output("q6-graph", "figure")
)
def update_q6_figure():
    # Gör om från bred form (en kolumn per region) till lång form (en rad per genre och region)
    long_df = df.melt(
        id_vars="genre",
        value_vars=list(REGION_NAMES.keys()),
        var_name="region",
        value_name="sales"
    )

    long_df["region"] = long_df["region"].map(REGION_NAMES)
 
    # Behåller de 3 genrerna med högst försäljning i varje region
    top3 = (
        long_df.dropna(subset=["sales"])
        .sort_values(["region", "sales"], ascending=[True, False])
        .groupby("region")
        .head(3)
    )
 
    # Sorterar regionerna i samma ordning som i REGION_NAMES
    region_order = list(REGION_NAMES.values())
 
    fig = px.bar(
        top3,
        x="genre",
        y="sales",
        color="genre",
        facet_col="region",
        category_orders={"region": region_order},
        labels={"sales": "Sales (millions)", "genre": "Genre", "region": "Region"},
        title="Top 3 genres per region"
    )
 
    # Varje region har sina egna genrer på x-axeln
    fig.update_xaxes(matches=None, showticklabels=True)
 
    # Plotly delar annars kategorilistan mellan alla paneler, vilket ger tomma platser.
    # Här begränsas varje panels x-axel till just den regionens 3 genrer.
    for col_index, region in enumerate(region_order, start=1):
        region_genres = top3.loc[top3["region"] == region, "genre"].tolist()
        fig.update_xaxes(
            categoryorder="array",
            categoryarray=region_genres,
            col=col_index
        )
 
    # Tar bort "region=" från rubrikerna ovanför varje panel
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    
    return fig