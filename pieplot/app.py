#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:24:07 2019

@author: divyachandran
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_ebola.csv')
df = df.dropna(axis=0)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1("Ebola Cases Reported in Africa - 2014")], style={"textAlign": "center"}),
    dcc.Graph(id="my-graph"),
    html.Div([dcc.Slider(
        id='month-selected',
        min=3,
        max=12,
        value=8,
        marks={
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December",
        },
    )
    ], style={
        'textAlign': "center", "margin": "30px", "padding": "10px"}),

], className="container")


@app.callback(
    dash.dependencies.Output("my-graph", "figure"),
    [dash.dependencies.Input("month-selected", "value")]
)
def update_graph(selected):
    return {
        "data": [go.Pie(
            labels=df["Country"].unique().tolist(),
            values=df[df["Month"] == selected]["Value"].tolist(),
            marker={'colors': ['#EF963B',
                               '#C93277',
                               '#349600',
                               '#EF533B',
                               '#57D4F1']},
            textinfo='label'

        )
        ],
        "layout": go.Layout(
            title=f"Cases Reported Monthly",
            margin={"l": 300, "r": 300, },
            legend={"x": 1, "y": 0.7}
        )

    }


server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
