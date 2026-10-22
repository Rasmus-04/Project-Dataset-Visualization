import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd
 
df = pd.read_pickle("data/preparedData/df_q13.pkl")
 
dash.register_page(
    __name__,
    path="/question-13",
    name="Question 13"
)
 
REGION_COLUMNS = ["na_sales", "jp_sales", "pal_sales", "other_sales"]
REGION_ORDER = ["North America", "Japan", "Europe and Africa", "Other"]
REGION_COLORS = {
    "North America": "#636EFA",
    "Japan": "#EF553B",
    "Europe and Africa": "#00CC96",
    "Other": "#AB63FA",
}
 
layout = html.Div([
    html.H2("Question 13: What titles are popular in one region but flop in another?"),
 
    html.Div([
        html.Div([
            html.Label("Show"),
            dcc.RadioItems(
                id="q13-mode",
                options=[
                    {"label": " Total sales by region", "value": "total"},
                    {"label": " Largest difference in regional share", "value": "share"},
                    {"label": " Largest difference from regional average", "value": "index"},
                ],
                value="total",
            ),
        ], style={"flex": "2"}),
 
        html.Div([
            html.Label("Number of titles"),
            dcc.Dropdown(
                id="q13-top-n",
                options=[{"label": f"Top {n}", "value": n} for n in [10, 20, 30, 50, 100]],
                value=20,
                clearable=False,
            ),
        ], style={"flex": "1", "marginRight": "30px"}),
 
        html.Div([
            html.Label("Minimum total sales (millions)"),
            dcc.Slider(
                id="q13-min-sales",
                min=0,
                max=10,
                step=0.5,
                value=1,
                marks={0: "0", 1: "1", 2: "2", 5: "5", 10: "10"}
            ),
        ], style={"flex": "2"}),
    ], style={"display": "flex", "marginBottom": "10px"}),
 
    html.P("Share and index views only include titles with recorded sales in all four regions."),
 
    dcc.Graph(id="q13-graph"),
])
 
 
@dash.callback(
    Output("q13-graph", "figure"),
    Input("q13-mode", "value"),
    Input("q13-top-n", "value"),
    Input("q13-min-sales", "value"),
)
def update_q13_figure(mode, top_n, min_sales):
    # Titlar med mycket låg försäljning kan få extrema andelar/index (t.ex. 100 % i en region) därför filtreras de bort innan rankingen
    sel = df[df["total_sales"] >= min_sales]
 
    # Varje läge använder olika kolumner, sortering och axeltext
    if mode == "total":
        suffix = ""
        sort_column = "total_sales"
        x_label = "Sales (millions)"
        title = "Best-selling titles and how their sales are split by region"
    elif mode == "share":
        suffix = "_share"
        sort_column = "sales_difference"
        x_label = "Share of the title's regional sales (%)"
        title = "Titles with the most uneven regional split"
    else:
        suffix = "_index"
        sort_column = "index_difference"
        x_label = "Sales index (1 = average title in that region)"
        title = "Titles that over- or underperform most compared with regional averages"
 
    # Andel och index finns bara för titlar med försäljning i alla fyra regioner (annars NaN)
    sel = sel.dropna(subset=[sort_column])
    top = sel.sort_values(sort_column, ascending=False).head(top_n)

 
    # en rad per titel och region
    value_columns = [column + suffix for column in REGION_COLUMNS]
    long_df = top.melt(
        id_vars="title",
        value_vars=value_columns,
        var_name="region",
        value_name="value",
    )

    # Byter namn på regionerna till ett mer läsbart namn
    long_df["region"] = long_df["region"].map(dict(zip(value_columns, REGION_ORDER)))
 
    fig = px.bar(
        long_df,
        x="value",
        y="title",
        color="region",
        orientation="h",
        barmode="group" if mode == "index" else "stack",
        category_orders={"title": top["title"].tolist(), "region": REGION_ORDER},
        color_discrete_map=REGION_COLORS,
        labels={"value": x_label, "title": "Title", "region": "Region"},
        title=title,
    )

    if mode == "index":
        fig.add_vline(x=1, line_dash="dash", line_color="gray", annotation_text="Regional average")
 
    # Höjden växer med antalet titlar (grupperade staplar behöver mer plats)
    row_height = 70 if mode == "index" else 30
    fig.update_layout(
        height=max(500, row_height * len(top) + 150),
        legend_title_text="Region"
    )
    return fig