import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Laddar iin den förberrada datframen
sales_by_platform_df = pd.read_pickle("data/preparedData/df_q1.pkl")

# Regional sales columns
regions = {
    "North America": "na_sales",
    "Japan": "jp_sales",
    "Europe and Africa": "pal_sales",
    "Other": "other_sales"
}

# Register the Dash page
dash.register_page(
    __name__,
    path="/question-1",
    name="Question 1"
)

# Page layout
layout = html.Div([
    html.H2(
        "Question 1: Which regions prefer which platform?"
    ),

# Region and number of platforms
    html.Div([
        html.Div([
            html.Label("Select region"),
            dcc.Dropdown(
                id="q1-region-dropdown",
                options=[{"label": region, "value": column} for region, column in regions.items()],
                value="na_sales",
                clearable=False
            )
        ], style={"flex": "1"}),

        html.Div([
            html.Label("Number of platforms"),
            dcc.Slider(
                id="q1-rows-slider",
                min=10,
                max=20,
                step=5,
                marks={10: "10", 15: "15", 20: "20"},
                value=15
            )
        ], style={"flex": "1"})

    ], style={
        "display": "flex",
        "gap": "20px",
        "maxWidth": "900px",
        "marginBottom": "20px"
    }),

    dcc.Graph(id="q1-platform-chart")
])


@dash.callback(
    Output("q1-platform-chart", "figure"),
    Input("q1-region-dropdown", "value"),
    Input("q1-rows-slider", "value")
)
def update_q1_graph(selected_region, nr_of_rows):
    # sätter region name till den valde regionen
    for region in regions:
        if selected_region == regions[region]:
            region_name = region
            break


    # Select {the nr_of_rows} platforms with the highest sales
    top_platforms_region_df = (
        sales_by_platform_df
        .nlargest(nr_of_rows, selected_region)  # hämtar de {the nr_of_rows} största värderna i den valde regionen 
        .sort_values(selected_region, ascending=True) # Sorterar efter storlek
    )

    
    fig = px.bar(
        top_platforms_region_df,
        x=selected_region,
        y="platform",
        orientation="h",
        title=f"Top {nr_of_rows} Gaming Platforms in {region_name}",
        labels={selected_region: "Sales (millions)",  "platform": "Platform"}
    )

    fig.update_layout(
        template="plotly_white",
        yaxis_title="Platform",
        xaxis_title="Sales (millions)",
        height=600
    )

    return fig
