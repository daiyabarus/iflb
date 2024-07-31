import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    [
        dcc.Graph(id="venn-diagram"),
        html.Div(
            [
                html.Label("A"),
                dcc.Slider(
                    id="slider-A",
                    min=-140,
                    max=-44,
                    step=1,
                    value=-100,
                    marks={i: str(i) for i in range(-140, -43, 10)},
                ),
            ],
            style={"width": "48%", "display": "inline-block"},
        ),
        html.Div(
            [
                html.Label("B"),
                dcc.Slider(
                    id="slider-B",
                    min=-140,
                    max=-44,
                    step=1,
                    value=-120,
                    marks={i: str(i) for i in range(-140, -43, 10)},
                ),
            ],
            style={"width": "48%", "display": "inline-block"},
        ),
        html.Div(
            [
                html.Label("C"),
                dcc.Slider(
                    id="slider-C",
                    min=-140,
                    max=-44,
                    step=1,
                    value=-90,
                    marks={i: str(i) for i in range(-140, -43, 10)},
                ),
            ],
            style={"width": "48%", "display": "inline-block"},
        ),
        html.Div(
            [
                html.Label("D"),
                dcc.Slider(
                    id="slider-D",
                    min=-140,
                    max=-44,
                    step=1,
                    value=-110,
                    marks={i: str(i) for i in range(-140, -43, 10)},
                ),
            ],
            style={"width": "48%", "display": "inline-block"},
        ),
    ]
)


# Define the callback to update the graph
@app.callback(
    Output("venn-diagram", "figure"),
    [
        Input("slider-A", "value"),
        Input("slider-B", "value"),
        Input("slider-C", "value"),
        Input("slider-D", "value"),
    ],
)
def update_graph(A, B, C, D):
    # Define the vertical lines
    vertical_lines = [
        {
            "type": "line",
            "x0": -35,
            "y0": -140,
            "x1": -35,
            "y1": -44,
            "line": {"color": "black", "width": 2},
        },
        {
            "type": "line",
            "x0": 35,
            "y0": -140,
            "x1": 35,
            "y1": -44,
            "line": {"color": "black", "width": 2},
        },
    ]

    # Define the connecting lines
    lines = [
        go.Scatter(x=[-40, -35], y=[A, A], mode="lines", line=dict(color="blue")),
        go.Scatter(x=[-40, -35], y=[B, B], mode="lines", line=dict(color="blue")),
        go.Scatter(x=[35, 40], y=[C, C], mode="lines", line=dict(color="blue")),
        go.Scatter(x=[35, 40], y=[D, D], mode="lines", line=dict(color="blue")),
        go.Scatter(
            x=[-35, 35],
            y=[(A + B) / 2, (C + D) / 2],
            mode="lines",
            line=dict(color="blue"),
        ),
    ]

    # Create the figure
    fig = go.Figure(data=lines)

    # Update layout
    fig.update_layout(
        shapes=vertical_lines,
        xaxis=dict(range=[-40, 40]),
        yaxis=dict(range=[-140, -44]),
    )

    return fig


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
