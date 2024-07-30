import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

st.set_page_config(layout="wide")


def create_graph(f1_values, f2_values):
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add lines and markers for F1 Cell (left y-axis)
    for name, value in f1_values.items():
        fig.add_trace(
            go.Scatter(
                x=[0],
                y=[value],
                mode="markers+text",
                name=f"{name} (F1)",
                text=[name],
                textposition="middle left",
                marker=dict(size=10, color=get_color(name)),
            ),
            secondary_y=False,
        )

    # Add lines and markers for F2 Cell (right y-axis)
    for name, value in f2_values.items():
        fig.add_trace(
            go.Scatter(
                x=[1],
                y=[value],
                mode="markers+text",
                name=f"{name} (F2)",
                text=[name],
                textposition="middle right",
                marker=dict(size=10, color=get_color(name)),
            ),
            secondary_y=True,
        )

    # Customize the layout
    fig.update_layout(
        title="Cellular Network Thresholds",
        xaxis=dict(
            tickvals=[0, 1],
            ticktext=["F1 Cell (Lower Prio)", "F2 Cell (Higher Prio)"],
            range=[-0.1, 1.1],
        ),
        yaxis=dict(title="RSRP for F1 Cell", side="left"),
        yaxis2=dict(title="RSRP for F2 Cell", side="right", overlaying="y"),
        showlegend=True,
        legend=dict(orientation="h", yanchor="top", y=-0.2, xanchor="center", x=0.5),
    )

    # Update y-axis ranges
    f1_min, f1_max = min(f1_values.values()), max(f1_values.values())
    f2_min, f2_max = min(f2_values.values()), max(f2_values.values())
    fig.update_yaxes(range=[f1_min - 5, f1_max + 5], secondary_y=False)
    fig.update_yaxes(range=[f2_min - 5, f2_max + 5], secondary_y=True)

    return fig


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


st.title("Cellular Network Threshold Visualizer")

# Input for F1 Cell
st.header("F1 Cell (Lower Priority)")
f1_a5threshold1rsrp = st.number_input("a5Threshold1Rsrp for F1", value=-110)
f1_threshxhigh = st.number_input("threshXHigh for F1", value=-100)
f1_a5threshold2rsrp = st.number_input("a5Threshold2Rsrp for F1", value=-105)
f1_qrxlevmin = st.number_input("qRxLevMin for F1", value=-120)

# Input for F2 Cell
st.header("F2 Cell (Higher Priority)")
f2_a5threshold1rsrp = st.number_input("a5Threshold1Rsrp for F2", value=-108)
f2_threshxlow = st.number_input("threshXLow for F2", value=-115)
f2_snoninttrasearch = st.number_input("sNonIntraSearch for F2", value=-106)
f2_threshservinglow = st.number_input("threshServingLow for F2", value=-112)
f2_a1a2searchthresholdrsrp = st.number_input(
    "a1a2SearchThresholdRsrp for F2", value=-110
)
f2_qrxlevmin = st.number_input("qRxLevMin for F2", value=-118)

if st.button("Generate Graph"):
    f1_values = {
        "a5Threshold1Rsrp": f1_a5threshold1rsrp,
        "threshXHigh": f1_threshxhigh,
        "a5Threshold2Rsrp": f1_a5threshold2rsrp,
        "qRxLevMin": f1_qrxlevmin,
    }
    f2_values = {
        "a5Threshold1Rsrp": f2_a5threshold1rsrp,
        "threshXLow": f2_threshxlow,
        "sNonIntraSearch": f2_snoninttrasearch,
        "threshServingLow": f2_threshservinglow,
        "a1a2SearchThresholdRsrp": f2_a1a2searchthresholdrsrp,
        "qRxLevMin": f2_qrxlevmin,
    }
    fig = create_graph(f1_values, f2_values)
    st.plotly_chart(fig)
