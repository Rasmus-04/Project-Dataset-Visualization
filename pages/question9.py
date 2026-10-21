import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd
 
df = pd.read_pickle("data/preparedData/df_q9.pkl")
 
dash.register_page(
    __name__,
    path="/question-9",
    name="Question 9"
)

 
# Alla tre alternativ: kolumn, axeltitel, textformat på stapeln
METRICS = {
    "total_sales": ("Total recorded sales (millions)", ":,.0f"),
    "share_of_total": ("Share of recorded sales (%)", ":.1f"),
    "avg_sales_per_record": ("Average sales per game with recorded sales (millions)", ":.2f"),
}
 
layout = html.Div([
    html.H2("Question 9: Which region purchases the most video games?"),
 
    html.Div([
        html.Label("Show"),
        dcc.RadioItems(
            id="q9-metric",
            options=[
                {"label": " Total sales (millions)", "value": "total_sales"},
                {"label": " Share of all recorded sales (%)", "value": "share_of_total"},
                {"label": " Average sales per game (millions)", "value": "avg_sales_per_record"},
            ],
            value="total_sales",
            inline=True,
            inputStyle={"marginLeft": "20px"},
        ),
    ], style={"marginBottom": "20px"}),
 
    dcc.Graph(id="q9-graph")
])
 
 
@dash.callback(
    Output("q9-graph", "figure"),
    Input("q9-metric", "value"),
)
def update_q9_figure(metric):
    y_label, text_format = METRICS[metric]
 
    # Sorterar så att regionen med högst värde hamnar längst till vänster
    plot_df = df.sort_values(metric, ascending=False)
 
    fig = px.bar(
        plot_df,
        x="region",
        y=metric,
        color="region",
        text=metric,
        hover_data={
            "total_sales": ":,.1f",
            "share_of_total": ":.1f",
            "records_with_sales": ":,",
            "avg_sales_per_record": ":.2f",
            "region": False,
        },
        labels={
            "region": "Region",
            metric: y_label,
            "total_sales": "Total sales (millions)",
            "share_of_total": "Share (%)",
            "records_with_sales": "Records with sales",
            "avg_sales_per_record": "Avg per game (millions)",
        },
        title="Video game sales by region",
    )
    fig.update_traces(texttemplate="%{text" + text_format + "}", textposition="outside")
    fig.update_layout(showlegend=False, yaxis_title=y_label)
    fig.update_yaxes(rangemode="tozero")
    return fig