import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

df = pd.read_pickle("data/preparedData/df_q4.pkl")

dash.register_page(
    __name__,
    path="/question-4",
    name="Question 4"
)

layout = dbc.Container([
    html.H2("Question 4: Which platforms for playing video games have been the most popular each release year?", className="mb-4"),

    dbc.Row([
        # Vänstra kolumnen: Line graph
        dbc.Col([dcc.Graph(id="q4-line-graph")], xs=12, lg=6),

        # Högra kolumnen: Heatmap
        dbc.Col([
            html.Label("Select release year range:"),

            dcc.RangeSlider(
                id="q4-year-range",
                min=int(df["release_year"].min()),
                max=int(df["release_year"].max()),
                value=[2000, 2024],
                marks={
                    year: str(year)
                    for year in range(
                        int(df["release_year"].min()) - (int(df["release_year"].min()) % 5),
                        int(df["release_year"].max()) + 1,
                        5
                    )
                },
                step=1,
                allowCross=False,
                tooltip={"placement": "bottom", "always_visible": True}
            ),

            html.Label("Number of platforms", className="mt-4"),

            dcc.Slider(
                id="nr-platforms-slider",
                min=10,
                max=30,
                step=5,
                marks={10: "10", 15: "15", 20: "20", 25: "25", 30: "30"},
                value=15
            ),

            dcc.Graph(id="q4-heat-graph")

        ], xs=12, lg=6)

    ], className="g-3")

], fluid=True)


@dash.callback(
    Output("q4-line-graph", "figure")
)
def update_q4_line_graph():
    # Create the line chart
    fig = px.line(
        df,
        x="release_year",
        y="total_sales",
        color="platform",
        markers=True,
        title="Worldwide Video Game Sales by Platform and Release Year",
        labels={
            "release_year": "Release year",
            "total_sales": "Worldwide sales (millions)",
            "platform": "Platform"
        },
        hover_data={
            "release_year": ":.0f",
            "total_sales": ":.2f",
            "platform": True
        }
    )

    # Improve chart readability
    fig.update_layout(
        xaxis_title="Release year",
        yaxis_title="Worldwide sales (millions)",
        legend_title="Platform",
        hovermode="closest",
        height=650
    )

    fig.update_xaxes(dtick=2)

    return fig


@dash.callback(
    Output("q4-heat-graph", "figure"),
    Input("q4-year-range", "value"),
    Input("nr-platforms-slider", "value")
    )
def update_q4_heat_graph(year_range, nr_of_platforms):
    # Filtrerar df till de valda åren
    filtered_df = df[df["release_year"].between(year_range[0], year_range[1])]

    # Väljder de nr_of_platforms platformana med hösta total_sales
    top_platforms = (
        filtered_df.groupby("platform")["total_sales"]
        .sum()
        .nlargest(nr_of_platforms)
        .index
    )

    # Filterar dataframen inom valt år så den bara inehåller data från top nr_of_platforms mest sålda platormana
    filtered_df = filtered_df[filtered_df["platform"].isin(top_platforms)]


    sales_matrix = filtered_df.pivot_table(
        index="platform",
        columns="release_year",
        values="total_sales",
        aggfunc="sum"
    )

    # Sort platforms by total sales
    sales_matrix = sales_matrix.loc[sales_matrix.sum(axis=1).sort_values(ascending=False).index]


    fig = px.imshow(
        sales_matrix,
        x=sales_matrix.columns,
        y=sales_matrix.index,
        color_continuous_scale="Viridis",
        labels={
            "x": "Release year",
            "y": "Platform",
            "color": "Sales in millions"
        },
        title=(f"Top {nr_of_platforms} Platforms by Worldwide Sales ({year_range[0]}–{year_range[1]})")
    )


    fig.update_layout(
        height=650,
        xaxis=dict(title="Release year", dtick=2),
        yaxis_title="Platform",
        coloraxis_colorbar_title="Sales in millions"
    )

    return fig
