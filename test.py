import plotly.graph_objs as go
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_vertical_slider import vertical_slider as svs


def create_slider(
    col,
    key,
    label,
    step,
    min_value,
    max_value,
    default_value,
    slider_color,
    track_color,
    thumb_color,
):
    with col:
        return svs(
            key=key,
            label=label,
            step=step,
            min_value=min_value,
            max_value=max_value,
            default_value=default_value,
            slider_color=slider_color,
            track_color=track_color,
            thumb_color=thumb_color,
            height=60,
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


def configure_sliders(columns):
    slider_values = {
        "a2criticalthresholdrsrp": create_slider(
            columns[0],
            "a2criticalthresholdrsrp",
            "a2CriticalThresholdRsrp",
            1,
            -140,
            -44,
            -123,
            "#2067CE",
            "lightgrey",
            "#5C59D3",
        ),
        "qrxlevmin": create_slider(
            columns[1],
            "qrxlevmin",
            "qRxLevMin SIB3",
            2,
            -140,
            -44,
            -120,
            "#2067CE",
            "lightgrey",
            "#5C59D3",
        ),
        "f1_threshxhigh": create_slider(
            columns[2],
            "threshxhigh",
            "threshXHigh",
            2,
            0,
            62,
            22,
            "#28BBDD",
            "lightgray",
            "#EA5D32",
        ),
        "f1_iflb_a5threshold1rsrp": create_slider(
            columns[3],
            "iflba5threshold1rsrp",
            "IFLB\na5Threshold1Rsrp",
            1,
            -140,
            -44,
            -60,
            "#28BBDD",
            "lightgray",
            "#EA5D32",
        ),
        "f1_iflb_a5threshold2rsrp": create_slider(
            columns[4],
            "iflba5threshold2rsrp",
            "IFLB a5Threshold2Rsrp",
            1,
            -140,
            -44,
            -96,
            "#28BBDD",
            "lightgray",
            "#EA5D32",
        ),
        "f2_threshservinglow": create_slider(
            columns[5],
            "f2threshservinglow",
            "threshServingLow",
            2,
            0,
            62,
            6,
            "#9CA3DB",
            "lightgray",
            "#E0CA3C",
        ),
        "f2_threshxlow": create_slider(
            columns[6],
            "f2_threshXLow",
            "threshXLow",
            2,
            0,
            62,
            6,
            "#9CA3DB",
            "lightgray",
            "#E0CA3C",
        ),
        "f2_snonintrasearch": create_slider(
            columns[7],
            "f2_snonintrasearch",
            "sNonIntraSearch",
            2,
            0,
            62,
            10,
            "#9CA3DB",
            "lightgray",
            "#E0CA3C",
        ),
        "f2_a1a2searchthresholdrsrp": create_slider(
            columns[8],
            "f2_a1a2searchthresholdrsrp",
            "a1a2SearchThresholdRsrp",
            1,
            -140,
            -44,
            -110,
            "#9CA3DB",
            "lightgray",
            "#E0CA3C",
        ),
        "f2_cov_a5threshold1rsrp": create_slider(
            columns[9],
            "f2_cov_a5threshold1rsrp",
            "COV a5Threshold1Rsrp",
            1,
            -140,
            -44,
            -112,
            "#9CA3DB",
            "lightgray",
            "#E0CA3C",
        ),
        "f2_cov_a5threshold2rsrp": create_slider(
            columns[10],
            "f2_cov_a5threshold2rsrp",
            "COV a5Threshold2Rsrp",
            1,
            -140,
            -44,
            -102,
            "#9CA3DB",
            "lightgray",
            "#E0CA3C",
        ),
        "f2_iflb_a5threshold1rsrp": create_slider(
            columns[11],
            "f2iflba5threshold1rsrp",
            "IFLB a5Threshold1Rsrp",
            1,
            -140,
            -44,
            -80,
            "#9CA3DB",
            "lightgray",
            "#E0CA3C",
        ),
        "f2_iflb_a5threshold2rsrp": create_slider(
            columns[12],
            "f2iflba5threshold2rsrp",
            "IFLB a5Threshold2Rsrp",
            1,
            -140,
            -44,
            -104,
            "#9CA3DB",
            "lightgray",
            "#E0CA3C",
        ),
    }
    return slider_values


def compute_threshold_mappings(sliders):
    f1_threshxhigh_map = (sliders["f1_threshxhigh"] * 2) + sliders["qrxlevmin"]
    f2_threshservinglow_map = (sliders["f2_threshservinglow"] * 2) + sliders[
        "qrxlevmin"
    ]
    f2_threshxlow_map = (sliders["f2_threshxlow"] * 2) + sliders["qrxlevmin"]
    f2_snonintrasearch_map = (sliders["f2_snonintrasearch"] * 2) + -124
    max_value = -44
    return (
        f1_threshxhigh_map,
        f2_threshservinglow_map,
        f2_threshxlow_map,
        f2_snonintrasearch_map,
        max_value,
    )


def create_vertical_lines(
    sliders, f1_threshxhigh_map, f2_threshservinglow_map, f2_threshxlow_map, max_value
):
    return [
        # TODO: F1 vline
        # vline 1
        create_vertical_line(-18, -140, sliders["qrxlevmin"]),
        create_vertical_line(-18, sliders["qrxlevmin"], -44, "green"),
        # vline 2
        create_vertical_line(-16, -140, f2_threshxlow_map),
        create_vertical_line(-16, f2_threshxlow_map, -44, "green"),
        # vline 3
        create_vertical_line(-14, -140, sliders["f2_cov_a5threshold2rsrp"]),
        create_vertical_line(-14, sliders["f2_cov_a5threshold2rsrp"], -44, "red"),
        # vline 4
        create_vertical_line(-12, -140, sliders["a2criticalthresholdrsrp"]),
        create_vertical_line(
            -12,
            sliders["a2criticalthresholdrsrp"],
            sliders["f1_iflb_a5threshold1rsrp"],
            "blue",
        ),
        create_vertical_line(-12, sliders["f1_iflb_a5threshold1rsrp"], -44),
        # vline 5
        create_vertical_line(-10, -140, sliders["f2_iflb_a5threshold2rsrp"]),
        create_vertical_line(-10, sliders["f2_iflb_a5threshold2rsrp"], -44, "blue"),
        # TODO: F2 vline
        # vline 1-1
        create_vertical_line(18, -140, sliders["a2criticalthresholdrsrp"]),
        create_vertical_line(
            18,
            sliders["a2criticalthresholdrsrp"],
            sliders["f2_iflb_a5threshold1rsrp"],
            "blue",
        ),
        create_vertical_line(18, sliders["f2_iflb_a5threshold1rsrp"], -44),
        # vline 1-2
        create_vertical_line(18, -140, f1_threshxhigh_map),
        create_vertical_line(18, f1_threshxhigh_map, -44, "green"),
        # vline 2
        create_vertical_line(19, -140, f2_threshservinglow_map),
        create_vertical_line(
            19, f2_threshservinglow_map, sliders["qrxlevmin"], "green"
        ),
        create_vertical_line(19, sliders["qrxlevmin"], -44),
        # vline 3-1
        create_vertical_line(16, -140, sliders["a2criticalthresholdrsrp"]),
        create_vertical_line(
            16,
            sliders["a2criticalthresholdrsrp"],
            sliders["f2_cov_a5threshold1rsrp"],
            "red",
        ),
        create_vertical_line(16, sliders["f2_cov_a5threshold1rsrp"], -44),
        # vline 3-2
        create_vertical_line(16, -140, sliders["f1_iflb_a5threshold2rsrp"]),
        create_vertical_line(16, sliders["f1_iflb_a5threshold2rsrp"], -44, "blue"),
    ]


def create_lines(
    sliders,
    f1_threshxhigh_map,
    f2_threshservinglow_map,
    f2_threshxlow_map,
    f2_snonintrasearch_map,
    max_value,
):
    return [
        go.Scatter(
            x=[-22, -18],
            y=[sliders["qrxlevmin"], sliders["qrxlevmin"]],
            mode="lines",
            line=dict(color="green", dash="dot"),
        ),
        go.Scatter(
            x=[-22, -10],
            y=[max_value, max_value],
            mode="lines",
            line=dict(color="gray", dash="dot"),
        ),
        go.Scatter(
            x=[-22, -16],
            y=[f2_threshxlow_map, f2_threshxlow_map],
            mode="lines",
            line=dict(color="green", dash="dot"),
        ),
        go.Scatter(
            x=[-22, -14],
            y=[sliders["f2_cov_a5threshold2rsrp"], sliders["f2_cov_a5threshold2rsrp"]],
            mode="lines",
            line=dict(color="red", dash="dot"),
        ),
        go.Scatter(
            x=[-22, -12],
            y=[sliders["a2criticalthresholdrsrp"], sliders["a2criticalthresholdrsrp"]],
            mode="lines+text",
            text=["a2CriticalThresholdRsrp"],
            textposition="middle left",
            textfont=dict(color="red", size=12),
            line=dict(color="red", dash="dot"),
        ),
        go.Scatter(
            x=[-22, -12],
            y=[
                sliders["f1_iflb_a5threshold1rsrp"],
                sliders["f1_iflb_a5threshold1rsrp"],
            ],
            mode="lines",
            line=dict(color="blue", dash="dot"),
        ),
        go.Scatter(
            x=[-22, -10],
            y=[
                sliders["f2_iflb_a5threshold2rsrp"],
                sliders["f2_iflb_a5threshold2rsrp"],
            ],
            mode="lines",
            line=dict(color="blue", dash="dot"),
        ),
        go.Scatter(
            x=[15, -8],
            y=[sliders["a2criticalthresholdrsrp"], sliders["a2criticalthresholdrsrp"]],
            mode="lines+text+markers",
            line=dict(color="red", shape="spline"),
            text=["", "A2 Critical HO"],
            textposition="top center",
            textfont=dict(color="red", size=15),
            marker=dict(symbol="arrow", size=15, angleref="previous"),
        ),
        go.Scatter(
            x=[20, 22],
            y=[f2_snonintrasearch_map, f2_snonintrasearch_map],
            mode="lines",
            line=dict(color="green", dash="dot"),
        ),
        go.Scatter(
            x=[19.5, 22],
            y=[
                sliders["f2_a1a2searchthresholdrsrp"],
                sliders["f2_a1a2searchthresholdrsrp"],
            ],
            mode="lines",
            line=dict(color="red", dash="dot"),
        ),
        go.Scatter(
            x=[18, 22],
            y=[
                sliders["f2_iflb_a5threshold1rsrp"],
                sliders["f2_iflb_a5threshold1rsrp"],
            ],
            mode="lines",
            line=dict(color="blue", dash="dot"),
        ),
        go.Scatter(
            x=[18, 22],
            y=[f1_threshxhigh_map, f1_threshxhigh_map],
            mode="lines",
            line=dict(color="green", dash="dot"),
        ),
        go.Scatter(
            x=[16, 22],
            y=[max_value, max_value],
            mode="lines",
            line=dict(color="gray", dash="dot"),
        ),
        go.Scatter(
            x=[19, 22],
            y=[sliders["qrxlevmin"], sliders["qrxlevmin"]],
            mode="lines",
            line=dict(color="green", dash="dot"),
        ),
        go.Scatter(
            x=[19, 22],
            y=[f2_threshservinglow_map, f2_threshservinglow_map],
            mode="lines",
            line=dict(color="green", dash="dot"),
        ),
        go.Scatter(
            x=[16, 22],
            y=[sliders["f2_cov_a5threshold1rsrp"], sliders["f2_cov_a5threshold1rsrp"]],
            mode="lines",
            line=dict(color="red", dash="dot"),
        ),
        go.Scatter(
            x=[16, 22],
            y=[sliders["a2criticalthresholdrsrp"], sliders["a2criticalthresholdrsrp"]],
            mode="lines",
            line=dict(color="grey", dash="dot"),
        ),
        go.Scatter(
            x=[16, 22],
            y=[
                sliders["f1_iflb_a5threshold2rsrp"],
                sliders["f1_iflb_a5threshold2rsrp"],
            ],
            mode="lines",
            line=dict(color="blue", dash="dot"),
        ),
        go.Scatter(
            x=[-18, -6, 6, 18],
            y=[
                ((sliders["qrxlevmin"] + max_value) / 2.5),
                ((sliders["qrxlevmin"] + max_value) / 2.5),
                ((f1_threshxhigh_map + max_value) / 2),
                ((f1_threshxhigh_map + max_value) / 2),
            ],
            line=dict(color="green", shape="spline", dash="dashdot"),
            marker=dict(symbol="arrow", size=20, angleref="previous"),
        ),
        go.Scatter(
            x=[-12, -4, 8, 16],
            y=[
                (
                    (
                        sliders["a2criticalthresholdrsrp"]
                        + sliders["f1_iflb_a5threshold1rsrp"]
                    )
                    / 2
                ),
                (
                    (
                        sliders["a2criticalthresholdrsrp"]
                        + sliders["f1_iflb_a5threshold1rsrp"]
                    )
                    / 2
                ),
                (sliders["f1_iflb_a5threshold2rsrp"] - max_value / 2),
                (sliders["f1_iflb_a5threshold2rsrp"] - max_value / 2),
            ],
            line=dict(color="blue", shape="spline", dash="dashdot"),
            marker=dict(symbol="arrow", size=20, angleref="previous"),
        ),
    ]


def configure_plot(
    sliders,
    f1_threshxhigh_map,
    f2_threshservinglow_map,
    f2_threshxlow_map,
    f2_snonintrasearch_map,
    max_value,
):
    vertical_lines = create_vertical_lines(
        sliders,
        f1_threshxhigh_map,
        f2_threshservinglow_map,
        f2_threshxlow_map,
        max_value,
    )
    lines = create_lines(
        sliders,
        f1_threshxhigh_map,
        f2_threshservinglow_map,
        f2_threshxlow_map,
        f2_snonintrasearch_map,
        max_value,
    )

    fig = go.Figure(data=lines)
    bottom_range = sliders["a2criticalthresholdrsrp"] - 4
    fig.update_layout(
        shapes=vertical_lines,
        xaxis=dict(range=[-22, 22], showticklabels=False, showgrid=False),
        yaxis=dict(
            range=[bottom_range, -40],
            showticklabels=False,
            showgrid=False,
            zeroline=False,
            showline=False,
        ),
        showlegend=False,
        height=800,
        margin=dict(
            autoexpand=False,
            l=300,
            r=300,
            t=100,
            b=100,
        ),
    )
    fig.add_vrect(
        x0=-22,
        x1=-20,
        fillcolor="grey",
        opacity=0.25,
        line_width=0,
    )
    fig.add_vrect(
        x0=20,
        x1=22,
        fillcolor="grey",
        opacity=0.25,
        line_width=0,
    )
    # Adding

    annotations = []

    y_data_left = [
        sliders["a2criticalthresholdrsrp"],
        sliders["qrxlevmin"],
        f2_threshxlow_map,
        sliders["f2_cov_a5threshold2rsrp"],
        sliders["f2_iflb_a5threshold2rsrp"],
        sliders["f1_iflb_a5threshold1rsrp"],
    ]

    y_data_right = [
        sliders["a2criticalthresholdrsrp"],
        sliders["qrxlevmin"],
        sliders["f2_cov_a5threshold1rsrp"],
        sliders["f2_a1a2searchthresholdrsrp"],
        f2_threshservinglow_map,
        f2_snonintrasearch_map,
        sliders["f1_iflb_a5threshold2rsrp"],
        sliders["f2_iflb_a5threshold1rsrp"],
        f1_threshxhigh_map,
    ]

    labels_left = [
        "a2CriticalThresholdRsrp",
        "qRxLevMin",
        "(set on F2)<br>threshXLow",
        "(set on F2)<br>ReportConfigA5 a5Threshold2Rsrp",
        "(set on F2)<br>ReportConfigEUtraInterFreqLb a5Threshold2Rsrp",
        "ReportConfigEUtraInterFreqLb a5Threshold1Rsrp",
    ]

    labels_right = [
        "a2CriticalThresholdRsrp",
        "qRxLevMin",
        "ReportConfigA5 a5Threshold1Rsrp",
        "a1a2SearchThresholdRsrp",
        "threshServingLow",
        "sNonIntraSearch",
        "(set on F1)<br>ReportConfigEUtraInterFreqLb a5Threshold2Rsrp",
        "ReportConfigEUtraInterFreqLb a5Threshold1Rsrp",
        "(set on F1)<br>threshXHigh",
    ]

    colors_left = ["red", "green", "green", "blue", "blue", "blue"]
    colors_right = [
        "red",
        "green",
        "red",
        "red",
        "green",
        "green",
        "blue",
        "blue",
        "green",
    ]

    for y_trace, label, color in zip(y_data_left, labels_left, colors_left):
        annotations.append(
            dict(
                x=-22,
                y=y_trace,
                xanchor="right",
                yanchor="middle",
                text=f"{label}",
                font=dict(family="Ericsson Hilda Light", size=12, color=color),
                showarrow=False,
                xref="x",
                yref="y",
            )
        )

    for y_trace, label, color in zip(y_data_right, labels_right, colors_right):
        annotations.append(
            dict(
                x=22,
                y=y_trace,
                xanchor="left",
                yanchor="middle",
                text=f"{label}",
                font=dict(family="Ericsson Hilda Light", size=12, color=color),
                showarrow=False,
                xref="x",
                yref="y",
            )
        )

    # Title
    annotations.append(
        dict(
            xref="paper",
            yref="paper",
            x=-0.05,
            y=1.1,
            xanchor="left",
            yanchor="bottom",
            text="Mobility Actions and Thresholds for the Priority Carrier Configuration",
            font=dict(family="Arial", size=30, color="rgb(37,37,37)"),
            showarrow=False,
        )
    )
    # Source
    annotations.append(
        dict(
            xref="paper",
            yref="paper",
            x=0.5,
            y=-0.1,
            xanchor="center",
            yanchor="top",
            text="Source: LTE Mobility and Traffic Management Guideline (4/154 43-LZA 701 6014 Uen Rev AL)",
            font=dict(family="Arial", size=12, color="rgb(150,150,150)"),
            showarrow=False,
        )
    )

    fig.add_annotation(
        x=21,
        y=1,
        text="F2 Cell<br>Higher Prio",
        showarrow=False,
        font=dict(size=14, family="Ericsson Hilda Light", color="rgb(150,150,150)"),
        xref="x",
        yref="paper",
        xanchor="center",
        yanchor="bottom",
    )
    fig.add_annotation(
        x=-21,
        y=1,
        text="F1 Cell<br>Lower Prio",
        showarrow=False,
        font=dict(size=14, family="Ericsson Hilda Light", color="rgb(150,150,150)"),
        xref="x",
        yref="paper",
        xanchor="center",
        yanchor="bottom",
    )
    fig.add_annotation(
        x=21,
        y=-0.01,
        text="🔻<br>Lowest<br>RSRP",
        showarrow=False,
        font=dict(size=14, family="Ericsson Hilda Light", color="rgb(150,150,150)"),
        xref="x",
        yref="paper",
        xanchor="center",
        yanchor="top",
    )
    fig.add_annotation(
        x=-21,
        y=-0.01,
        text="🔻<br>Lowest<br>RSRP",
        showarrow=False,
        font=dict(size=14, family="Ericsson Hilda Light", color="rgb(150,150,150)"),
        xref="x",
        yref="paper",
        xanchor="center",
        yanchor="top",
    )
    fig.update_layout(annotations=annotations)

    return fig


def run_priority():

    columns = st.columns(13)
    sliders = configure_sliders(columns)
    (
        f1_threshxhigh_map,
        f2_threshservinglow_map,
        f2_threshxlow_map,
        f2_snonintrasearch_map,
        max_value,
    ) = compute_threshold_mappings(sliders)
    fig = configure_plot(
        sliders,
        f1_threshxhigh_map,
        f2_threshservinglow_map,
        f2_threshxlow_map,
        f2_snonintrasearch_map,
        max_value,
    )

    with stylable_container(
        key="container_with_border",
        css_styles="""
            {
                border: 2px solid rgba(49, 51, 63, 0.2);
                border-radius: 0.5rem;
                padding: calc(1em - 1px)
            }
            """,
    ):
        container = st.container()
        with container:
            st.plotly_chart(fig, use_container_width=False)


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
