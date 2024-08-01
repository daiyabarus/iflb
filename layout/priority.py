import plotly.graph_objs as go
import streamlit as st
from streamlit_vertical_slider import vertical_slider as svs

# Constants
MAX_VALUE = -44
MIN_VALUE = -140
SLIDER_HEIGHT = 100


def create_slider(key, label, min_value, max_value, default_value, color, thumb_color):
    return svs(
        key=key,
        label=label,
        step=2,
        min_value=min_value,
        max_value=max_value,
        default_value=default_value,
        slider_color=color,
        track_color="lightgray",
        thumb_color=thumb_color,
        height=SLIDER_HEIGHT,
        value_always_visible=True,
    )


def create_vertical_line(x, y0, y1, color="rgba(0,0,0,0)", width=2):
    return {
        "type": "line",
        "x0": x,
        "y0": y0,
        "x1": x,
        "y1": y1,
        "line": {"color": color, "width": width},
    }


def create_scatter(x, y, color):
    return go.Scatter(
        x=x,
        y=y,
        mode="lines+markers",
        line=dict(color=color),
    )


def create_layout(vertical_lines):
    return go.Layout(
        shapes=vertical_lines,
        xaxis=dict(range=[-60, 60], showticklabels=False, showgrid=False),
        yaxis=dict(
            range=[MIN_VALUE, MAX_VALUE],
            showticklabels=False,
            showgrid=False,
            zeroline=False,
            showline=False,
        ),
        showlegend=False,
        height=700,
    )


def run_priority():
    st.title("Mobility Actions and Thresholds for the Priority Carrier Configuration")

    # Create a single row with multiple columns
    cols = st.columns(11)

    # Define slider configurations
    slider_configs = [
        (
            "a2criticalthresholdrsrp",
            "a2CriticalThresholdRsrp",
            MIN_VALUE,
            MAX_VALUE,
            -123,
            "#2067CE",
            "#5C59D3",
        ),
        (
            "qrxlevmin",
            "qRxLevMin SIB3",
            MIN_VALUE,
            MAX_VALUE,
            -120,
            "#28BBDD",
            "#EA5D32",
        ),
        ("threshxhigh", "threshXHigh", 0, 62, 16, "#28BBDD", "#EA5D32"),
        (
            "iflba5threshold1rsrp",
            "ReportConfigEUtraInterFreqLb a5Threshold1Rsrp",
            MIN_VALUE,
            MAX_VALUE,
            -100,
            "#28BBDD",
            "#EA5D32",
        ),
        (
            "iflba5threshold2rsrp",
            "ReportConfigEUtraInterFreqLb a5Threshold2Rsrp",
            MIN_VALUE,
            MAX_VALUE,
            -110,
            "#28BBDD",
            "#EA5D32",
        ),
        (
            "f2qrxlevmin",
            "qRxLevMin SIB3",
            MIN_VALUE,
            MAX_VALUE,
            -120,
            "#9CA3DB",
            "#E0CA3C",
        ),
        ("f2threshxlow", "threshXLow", 0, 62, 6, "#9CA3DB", "#E0CA3C"),
        ("f2threshservinglow", "threshServingLow", 0, 62, 2, "#9CA3DB", "#E0CA3C"),
        (
            "f2cova5threshold1rsrp",
            "ReportConfigA5 a5Threshold1Rsrp",
            MIN_VALUE,
            MAX_VALUE,
            -108,
            "#9CA3DB",
            "#E0CA3C",
        ),
        (
            "f2cova5threshold2rsrp",
            "ReportConfigA5 a5Threshold2Rsrp",
            MIN_VALUE,
            MAX_VALUE,
            -110,
            "#9CA3DB",
            "#E0CA3C",
        ),
        (
            "f2iflba5threshold1rsrp",
            "ReportConfigEUtraInterFreqLb a5Threshold1Rsrp",
            MIN_VALUE,
            MAX_VALUE,
            -90,
            "#9CA3DB",
            "#E0CA3C",
        ),
    ]

    # Create sliders in a single row
    sliders = {}
    for col, config in zip(cols, slider_configs):
        with col:
            key, label, min_val, max_val, default, color, thumb = config
            sliders[key] = create_slider(
                key, label, min_val, max_val, default, color, thumb
            )

    # Calculate mapped values
    f2_threshxlow_map = (sliders["f2threshxlow"] * 2) + sliders["f2qrxlevmin"]
    f1_threshxhigh_map = (sliders["threshxhigh"] * 2) + sliders["qrxlevmin"]
    f2_threshservinglow_map = (sliders["f2threshservinglow"] * 2) + sliders[
        "f2qrxlevmin"
    ]

    # Create vertical lines and scatter plots
    vertical_lines = [
        create_vertical_line(-45, MIN_VALUE, sliders["qrxlevmin"], "green"),
        create_vertical_line(-45, sliders["qrxlevmin"], MAX_VALUE, "green"),
        create_vertical_line(-40, MIN_VALUE, f2_threshxlow_map, "green"),
        create_vertical_line(-40, f2_threshxlow_map, MAX_VALUE, "green"),
        create_vertical_line(-35, MIN_VALUE, sliders["f2cova5threshold2rsrp"], "red"),
        create_vertical_line(-35, sliders["f2cova5threshold2rsrp"], MAX_VALUE, "red"),
        # Add more vertical lines as needed
    ]

    scatter_plots = [
        create_scatter(
            [-50, -45], [sliders["qrxlevmin"], sliders["qrxlevmin"]], "green"
        ),
        create_scatter([-50, -45], [MAX_VALUE, MAX_VALUE], "green"),
        create_scatter([-50, -40], [f2_threshxlow_map, f2_threshxlow_map], "green"),
        create_scatter([-50, -40], [MAX_VALUE, MAX_VALUE], "green"),
        create_scatter(
            [-50, -35],
            [sliders["f2cova5threshold2rsrp"], sliders["f2cova5threshold2rsrp"]],
            "red",
        ),
        create_scatter([-50, -35], [MAX_VALUE, MAX_VALUE], "red"),
        # Add more scatter plots as needed
    ]

    # Create figure
    fig = go.Figure(data=scatter_plots, layout=create_layout(vertical_lines))

    # Use a container for the Plotly chart
    with st.container():
        st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    st.markdown(
        """
        <style>
        [data-testid="collapsedControl"] {
                display: none;
            }
        #MainMenu, header, footer {visibility: hidden;}
        .appview-container .main .block-container {
            padding-top: 1px;
            padding-left: 1rem;
            padding-right: 1rem;
            padding-bottom: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    run_priority()
