import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly as plt

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

available_indicators = ['Sex', 'Age', 'Education', 'Income', 'BrandOwn', 'BMW', 'Ford', 'Mercedes', 'Toyota']

df = pd.read_csv('Book1.csv')

df1 = pd.read_csv('Book3.csv')

dff = df.groupby(['Brand']).mean()

fig = px.scatter(dff, x="Evaluation", y="Activity", size='Potency', text=['BMW', 'Ford', 'Mercedes', 'Toyota'])

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='crossfilter-xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators]
            )
        ],
            style={'width': '49%', 'display': 'inline-block'}),

    ], style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'
    }),

    html.Div([
        dcc.Graph(id='crossfilter-indicator-scatter', figure=fig)
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),

])


@app.callback(
    dash.dependencies.Output('crossfilter-indicator-scatter', 'figure'),
    [dash.dependencies.Input('crossfilter-xaxis-column', 'value')
     ])
def update_graph(xaxis_column_name):
    brand = ['BMW', 'Ford', 'Mercedes', 'Toyota']
    dff = df.groupby(['Brand']).mean()
    fig = px.scatter(dff, x="Evaluation", y="Activity", size='Potency', text=brand, color=brand)

    if xaxis_column_name == 'Age':
        brand = ['BMW', 'BMW', 'BMW', 'BMW', 'BMW', 'Ford', 'Ford', 'Ford', 'Ford', 'Ford', 'Mercedes', 'Mercedes', 'Mercedes', 'Mercedes', 'Mercedes', 'Toyota', 'Toyota', 'Toyota', 'Toyota', 'Toyota']
        dff = df.groupby(['Brand', 'Age']).mean()
        fig = px.scatter(dff, x="Evaluation", y="Activity", size='Potency', text=['1', '2', '3', '4', '5', '1', '2', '3', '4', '5', '1', '2', '3', '4', '5', '1', '2', '3', '4', '5'], color=brand)

    if xaxis_column_name == 'Education':
        brand = ['BMW', 'BMW', 'BMW', 'BMW', 'BMW', 'Ford', 'Ford', 'Ford', 'Ford', 'Ford', 'Mercedes', 'Mercedes', 'Mercedes', 'Mercedes', 'Mercedes', 'Toyota', 'Toyota', 'Toyota', 'Toyota', 'Toyota']
        dff = df.groupby(['Brand', 'Education']).mean()
        fig = px.scatter(dff, x="Evaluation", y="Activity", size='Potency', text=['1', '2', '3', '4', '5', '1', '2', '3', '4', '5', '1', '2', '3', '4', '5', '1', '2', '3', '4', '5'], color=brand)

    if xaxis_column_name == 'Sex':
        brand = ['BMW', 'BMW', 'Ford', 'Ford', 'Mercedes', 'Mercedes', 'Toyota', 'Toyota']
        dff = df.groupby(['Brand', 'Sex']).mean()
        fig = px.scatter(dff, x="Evaluation", y="Activity", size='Potency', text=['1', '2', '1', '2', '1', '2', '1', '2'], color=brand)

    if xaxis_column_name == 'Income':
        brand = ['BMW', 'BMW', 'BMW', 'BMW', 'BMW', 'Ford', 'Ford', 'Ford', 'Ford', 'Ford', 'Mercedes', 'Mercedes', 'Mercedes', 'Mercedes', 'Mercedes', 'Toyota', 'Toyota', 'Toyota', 'Toyota', 'Toyota']
        dff = df.groupby(['Brand', 'Income']).mean()
        fig = px.scatter(dff, x="Evaluation", y="Activity", size='Potency', text=['1', '2', '3', '4', '5', '1', '2', '3', '4', '5', '1', '2', '3', '4', '5', '1', '2', '3', '4', '5'], color=brand)

    if xaxis_column_name == 'BrandOwn':
        brand = ['BMW', 'BMW', 'Ford', 'Ford', 'Mercedes', 'Mercedes', 'Toyota', 'Toyota']
        dff = df.groupby(['Brand', 'BrandOwn']).mean()
        fig = px.scatter(dff, x="Evaluation", y="Activity", size='Potency', text=['0', '1', '0', '1', '0', '1', '0', '1'], color=brand)

    if xaxis_column_name == 'BMW':
        text = ['BMW', 'mother', 'fiancé', 'companion', 'friend', 'loved one']
        color = df1['BDistance']
        fig = px.scatter(df1, x="BMeanE", y="BMeanA", size="BMeanP", color=color, text=text)

    if xaxis_column_name == 'Ford':
        text = ['Ford', 'employer', 'millionaire', 'Marine Corps officer', 'grownup', 'principal']
        color = df1['FDistance']
        fig = px.scatter(df1, x="FMeanE", y="FMeanA", size="FMeanP", color=color, text=text)

    if xaxis_column_name == 'Mercedes':
        text = ['Mercedes', 'loved one', 'fiancé', 'companion', 'mother', 'true love']
        color = df1['MDistance']
        fig = px.scatter(df1, x="MMeanE", y="MMeanA", size="MMeanP", color=color, text=text)

    if xaxis_column_name == 'Toyota':
        text = ['Toyota', 'helper', 'pediatrician', 'registered nurse', 'practical nurse', 'sweetheart']
        color = df1['TDistance']
        fig = px.scatter(df1, x="TMeanE", y="TMeanA", size="TMeanP", color=color, text=text)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
