import pandas as pd
import numpy as np
import matplotlib as plt
from scipy import stats
from dash import Dash, html, dcc
import plotly.express as px

import datetime
import os
import re

# -*- coding: utf-8 -*-
from dash import Dash, dcc, html, Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

all_options = [
            {'label': 'Wake up', 'value': 'Wake up'},
            {'label': 'Eat', 'value': 'Eat'},
            {'label': 'Go to work', 'value': 'Go to work'},
        ]

all_posibilities = [i['label'] for i in all_options]

app.layout = html.Div([
    html.Div('To do list: '),
    dcc.Checklist(
        options=all_options,
        id='activities'
    ),
    html.Hr(),
    html.Div(id='display finished activities')
])


@app.callback(
    Output('display finished activities', 'children'),
    Input('activities', 'value'))
def set_activity_options(activity):
    if not activity:
        return "No activity done. Get to work!"
    elif activity == all_posibilities:
        return "All activities are done."
    else:
        return [f"{i} has been done.\n" for i in activity]


if __name__ == '__main__':
    app.run_server(debug=True, port='8050')