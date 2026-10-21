import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd
 
df = pd.read_pickle("data/preparedData/df_q10.pkl")

dropdown_options = [{"label": f"Top {n}", "value": n} for n in [10, 15, 25, 50]]

dash.register_page(
    __name__,
    path="/question-10",
    name="Question 10"
)
 
layout = html.Div([
    html.H2("Question 10: Which titles sold the most worldwide?"),
 
    html.Div([
        html.Label("Number of titles to show"),
        dcc.Dropdown(
            id="q10-top-n",
            options=dropdown_options,
            value=10,
            clearable=False,
        ),
    ], style={"width": "250px", "marginBottom": "20px"}),
 
    dcc.Graph(id="q10-graph")
])
 

@dash.callback(
    Output("q10-graph", "figure"),
    Input("q10-top-n", "value"),
)
def update_q10_figure(top_n):
    top = df.head(top_n)
 
    fig = px.bar(
        top,
        x="worldwide_sales",
        y="title",
        orientation="h",
        text="worldwide_sales",
        labels={"worldwide_sales": "Worldwide sales (millions)", "title": "Title"},
        title=f"Top {top_n} best-selling titles worldwide",
    )
    fig.update_traces(texttemplate="%{text:.1f}", textposition="outside")
    fig.update_layout(
        # Högst försäljning överst
        yaxis={"categoryorder": "total ascending"},
        # Höjden växer med antalet titlar så att namnen alltid är läsbara
        height=max(450, 28 * top_n + 150),
        margin={"l": 260}
    )
    fig.update_xaxes(rangemode="tozero")
    return fig