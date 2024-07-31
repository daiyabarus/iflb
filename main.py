import plotly.graph_objs as go
import streamlit as st

# import streamlit_vertical_slider as svs
from streamlit_vertical_slider import vertical_slider as svs

st.set_page_config(layout="wide")
# Streamlit layout
st.title("Mobility Actions and Thresholds for the Priority Carrier Configuration")

# Create four columns for sliders
col1, col2, col3, col4, _, _, _, _, _, _ = st.columns(10)

# Vertical sliders in one row
with col1:
    A = svs(
        key="A",
        label="A",
        step=1,
        min_value=-140,
        max_value=-44,
        default_value=-100,
        slider_color="green",
        track_color="lightgray",
        thumb_color="red",
        height=100,
        value_always_visible=True,
    )
with col2:
    B = svs(
        key="B", min_value=-140, max_value=-44, default_value=-120, step=1, label="B"
    )
with col3:
    C = svs(
        key="C", min_value=-140, max_value=-44, default_value=-90, step=1, label="C"
    )
with col4:
    D = svs(
        key="D", min_value=-140, max_value=-44, default_value=-110, step=1, label="D"
    )


# Define the vertical line segments
def create_vertical_line(x, y0, y1, color="rgba(0,0,0,0)", width=2):
    return {
        "type": "line",
        "x0": x,
        "y0": y0,
        "x1": x,
        "y1": y1,
        "line": {"color": color, "width": width},
    }


vertical_lines = [
    create_vertical_line(-35, -140, B),
    create_vertical_line(-35, B, A, "blue"),
    create_vertical_line(-35, A, -44),
    create_vertical_line(35, -140, D),
    create_vertical_line(35, D, C, "red"),
    create_vertical_line(35, C, -44),
]

# Define the connecting lines
lines = [
    go.Scatter(x=[-40, -35], y=[A, A], mode="lines", line=dict(color="blue")),
    go.Scatter(x=[-40, -35], y=[B, B], mode="lines", line=dict(color="green")),
    go.Scatter(x=[35, 40], y=[C, C], mode="lines", line=dict(color="red")),
    go.Scatter(x=[35, 40], y=[D, D], mode="lines", line=dict(color="gray")),
    go.Scatter(
        x=[-35, 35],
        y=[(A + B) / 2, (C + D) / 2],
        mode="lines+markers",
        line=dict(color="blue", shape="spline"),
        marker=dict(symbol="arrow", size=15, angleref="previous"),
    ),
]

# Create the figure
fig = go.Figure(data=lines)

# Update layout
fig.update_layout(
    shapes=vertical_lines,
    xaxis=dict(range=[-40, 40], showticklabels=False, showgrid=False),
    yaxis=dict(
        range=[-140, -44],
        showticklabels=False,
        showgrid=False,
        zeroline=False,
        showline=False,
    ),
    showlegend=False,
    width=1500,
    height=700,
)

# Display the figure after the sliders
st.plotly_chart(fig)
