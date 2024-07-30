import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots
from streamlit_vertical_slider import vertical_slider


def create_vertical_slider(key, min_value=-140, max_value=-80, default_value=-110):
    return vertical_slider(
        key=key,
        min_value=min_value,
        max_value=max_value,
        default_value=default_value,
        step=1,
        slider_color="#1E90FF",
        track_color="#D3D3D3",
        thumb_color="#1E90FF",
    )


def create_graph(f1_values, f2_values):
    fig = go.Figure()
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add vertical line for the shared axis
    fig.add_vline(x=0, line_width=2, line_dash="dash", line_color="#FFFFFF")
    fig.add_vline(x=-18, line_width=2, line_dash="dash", line_color="blue")
    fig.add_vline(x=18, line_width=2, line_dash="dash", line_color="blue")

    # Add markers and lines for F1 Cell
    for name, value in f1_values.items():
        fig.add_trace(
            go.Scatter(
                x=[-20],
                y=[value],
                mode="markers+text",
                name=f"{name} (F1)",
                text=[name],
                textposition="middle left",
                marker=dict(size=10, color=get_color(name)),
            )
        )

    # Add markers and lines for F2 Cell
    for name, value in f2_values.items():
        fig.add_trace(
            go.Scatter(
                x=[20],
                y=[value],
                mode="markers+text",
                name=f"{name} (F2)",
                text=[name],
                textposition="middle right",
                marker=dict(size=10, color=get_color(name)),
            )
        )

    # Connect parameters with lines
    connect_parameters(fig, f1_values, f2_values)

    # Update layout
    fig.update_layout(
        title="IFLB Visual Illustrated",
        showlegend=False,
        height=600,
        yaxis=dict(range=[-140, -44], title="RSRP (dBm)"),
        xaxis=dict(showticklabels=False, range=[-21, 21]),
    )

    return fig


def connect_parameters(fig, f1_values, f2_values):
    parameters_to_connect = [
        ("a5Threshold1Rsrp", "a5Threshold1Rsrp"),
        ("a5Threshold2Rsrp", "a5Threshold2Rsrp"),
        ("qRxLevMin", "threshXLow"),
    ]

    for f1_param, f2_param in parameters_to_connect:
        if f1_param in f1_values and f2_param in f2_values:
            if f1_param == "qRxLevMin" and f2_param == "threshXLow":
                fig.add_trace(
                    go.Scatter(
                        x=[-18, 18],
                        y=[f1_values[f1_param], f2_values[f2_param]],
                        mode="lines+markers",
                        line=dict(color=get_color(f1_param), width=2),
                        showlegend=False,
                    )
                )
            else:
                fig.add_trace(
                    go.Scatter(
                        x=[-20, 0, 20],
                        y=[
                            f1_values[f1_param],
                            (f1_values[f1_param] + f2_values[f2_param]) / 2,
                            f2_values[f2_param],
                        ],
                        mode="lines+markers",
                        line=dict(color=get_color(f1_param), width=2),
                        showlegend=False,
                    )
                )


def get_color(name):
    color_map = {
        "a5Threshold1Rsrp": "blue",
        "a5Threshold2Rsrp": "red",
        "threshXHigh": "green",
        "threshXLow": "orange",
        "sNonIntraSearch": "purple",
        "threshServingLow": "brown",
        "a1a2SearchThresholdRsrp": "pink",
        "qRxLevMin": "cyan",
        "a2CriticalThresholdRsrp": "magenta",
    }
    return color_map.get(name, "gray")


st.set_page_config(layout="wide")
st.title("IFLB Visual Illustrated")

col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    st.header("F1 Cell")
    f1_a5threshold1rsrp = create_vertical_slider("a5Threshold1Rsrp (F1)")
    f1_a5threshold2rsrp = create_vertical_slider("a5Threshold2Rsrp (F1)")
    f1_threshxhigh = create_vertical_slider("threshXHigh (F1)")
    f1_qrxlevmin = create_vertical_slider("qRxLevMin (F1)")

with col3:
    st.header("F2 Cell")
    f2_a5threshold1rsrp = create_vertical_slider("a5Threshold1Rsrp (F2)")
    f2_a5threshold2rsrp = create_vertical_slider("a5Threshold2Rsrp (F2)")
    f2_threshxlow = create_vertical_slider("threshXLow (F2)")
    f2_snoninttrasearch = create_vertical_slider("sNonIntraSearch (F2)")
    f2_threshservinglow = create_vertical_slider("threshServingLow (F2)")
    f2_qrxlevmin = create_vertical_slider("qRxLevMin (F2)")

f1_values = {
    "a5Threshold1Rsrp": f1_a5threshold1rsrp,
    "a5Threshold2Rsrp": f1_a5threshold2rsrp,
    "threshXHigh": f1_threshxhigh,
    "qRxLevMin": f1_qrxlevmin,
}
f2_values = {
    "a5Threshold1Rsrp": f2_a5threshold1rsrp,
    "a5Threshold2Rsrp": f2_a5threshold2rsrp,
    "threshXLow": f2_threshxlow,
    "sNonIntraSearch": f2_snoninttrasearch,
    "threshServingLow": f2_threshservinglow,
    "qRxLevMin": f2_qrxlevmin,
}

with col2:
    fig = create_graph(f1_values, f2_values)
    st.plotly_chart(fig, use_container_width=True)
