from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

quakes = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')
app = Dash()

app.layout = [
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.RangeSlider(min=quakes.Magnitude.min(), max=quakes.Magnitude.max(), step=0.5, value=[quakes.Magnitude.min(), quakes.Magnitude.max()], id='magnitude-range'),
    dcc.Graph(id='graph-content')
]

@callback(
    Output('graph-content', 'figure'),
    Input('magnitude-range', 'value')
)
def update_graph(value):
    df = quakes[(quakes.Magnitude>=value[0]) & (quakes.Magnitude<=value[1])]
    fig = go.Figure(go.Scattermap(lat=df.Latitude, lon=df.Longitude, mode='markers',
    text=df["Magnitude"],
    marker=dict(
        size=10,
        color=df.Magnitude, #set color equal to a variable
        cmin=quakes.Magnitude.min(),
        cmax=quakes.Magnitude.max(),
        opacity=0.4,
        colorscale='Viridis', # one of plotly colorscales
        showscale=True
    )))
    fig.update_layout(map_style="carto-positron", map_center_lon=180)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

if __name__ == '__main__':
    app.run(debug=True)
