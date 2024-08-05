import plotly.graph_objs as go
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_vertical_slider import vertical_slider as svs

from layout.styles import multi_color_styling


def create_slider(
    col,
    key,
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
            1,
            -140,
            -44,
            -123,
            "#AAE89F",
            "lightgrey",
            "#5DC93E",
        ),
        "qrxlevminsib1": create_slider(
            columns[1],
            "qrxlevminsib1",
            2,
            -140,
            -44,
            -124,
            "#AAE89F",
            "lightgrey",
            "#5DC93E",
        ),
        "qrxlevmin": create_slider(
            columns[2],
            "qrxlevmin",
            2,
            -140,
            -44,
            -120,
            "#AAE89F",
            "lightgrey",
            "#5DC93E",
        ),
        "f1_snonintrasearch": create_slider(
            columns[3],
            "f1_snonintrasearch",
            2,
            0,
            62,
            8,
            "#AAE89F",
            "lightgrey",
            "#5DC93E",
        ),
        "f1_threshservinglow": create_slider(
            columns[4],
            "f1threshservinglow",
            2,
            0,
            62,
            4,
            "#AAE89F",
            "lightgrey",
            "#5DC93E",
        ),
        "f1_threshxlow": create_slider(
            columns[5],
            "f1_threshXLow",
            2,
            0,
            62,
            6,
            "#AAE89F",
            "lightgrey",
            "#5DC93E",
        ),
        "f1_a1a2searchthresholdrsrp": create_slider(
            columns[6],
            "f1_a1a2searchthresholdrsrp",
            1,
            -140,
            -44,
            -110,
            "#FA0101",
            "lightgray",
            "#C1392B",
        ),
        "f1_cov_a5threshold1rsrp": create_slider(
            columns[7],
            "f1_cov_a5threshold1rsrp",
            1,
            -140,
            -44,
            -113,
            "#FA0101",
            "lightgray",
            "#C1392B",
        ),
        "f1_cov_a5threshold2rsrp": create_slider(
            columns[8],
            "f1_cov_a5threshold2rsrp",
            1,
            -140,
            -44,
            -106,
            "#FA0101",
            "lightgray",
            "#C1392B",
        ),
        "f1_iflb_a5threshold1rsrp": create_slider(
            columns[9],
            "iflba5threshold1rsrp",
            1,
            -140,
            -44,
            -50,
            "#0000FF",
            "lightgray",
            "#F1C40F",
        ),
        "f1_iflb_a5threshold2rsrp": create_slider(
            columns[10],
            "iflba5threshold2rsrp",
            1,
            -140,
            -44,
            -96,
            "#0000FF",
            "lightgray",
            "#F1C40F",
        ),
    }
    return slider_values


def generate_scripts(sliders):
    script_lines = [
        "# SET ON F1",
        f'set `F1` A2Critical {sliders["a2criticalthresholdrsrp"]} dBm',
        f'set `F1` QRxLevMin {sliders["qrxlevminsib1"]} dBm ',
        f'set `F1` SIB3 sNonIntraSearch {sliders["f1_snonintrasearch"]} dB',
        f'set `F1` threshServingLow {sliders["f1_threshservinglow"]} dB',
        f'set `F1` EUtranFreq `F2` threshXLow {sliders["f1_threshxlow"]} dB',
        f'set `F1` A1A2 SearchThreshold RSRP {sliders["f1_a1a2searchthresholdrsrp"]} dBm',
        f'set `F1` COV A5Threshold1 {sliders["f1_cov_a5threshold1rsrp"]} dBm',
        f'set `F1` COV A5Threshold2 {sliders["f1_cov_a5threshold2rsrp"]} dBm',
        f'set `F1` IFLB A5Threshold1 {sliders["f1_iflb_a5threshold1rsrp"]} dBm',
        f'set `F1` IFLB A5Threshold2 {sliders["f1_iflb_a5threshold2rsrp"]} dBm',
    ]

    script = "\n".join(script_lines)
    return script


def compute_threshold_mappings(sliders):
    f1_threshservinglow_map = (sliders["f1_threshservinglow"] * 2) + sliders[
        "qrxlevmin"
    ]
    f1_threshxlow_map = (sliders["f1_threshxlow"] * 2) + sliders["qrxlevmin"]
    f1_snonintrasearch_map = (sliders["f1_snonintrasearch"] * 2) + sliders[
        "qrxlevminsib1"
    ]
    max_value = -44
    return (
        f1_threshservinglow_map,
        f1_threshxlow_map,
        f1_snonintrasearch_map,
        max_value,
    )


def create_vertical_lines(
    sliders,
    f1_threshservinglow_map,
    f1_threshxlow_map,
    max_value=-44,
):
    return [
        create_vertical_line(-9, -140, sliders["qrxlevmin"]),
        create_vertical_line(
            -9,
            sliders["qrxlevmin"],
            f1_threshservinglow_map,
            "green",
        ),
        create_vertical_line(-9, -140, f1_threshservinglow_map),
        create_vertical_line(
            -9, f1_threshservinglow_map, sliders["qrxlevmin"], "green"
        ),
        create_vertical_line(
            -8,
            sliders["a2criticalthresholdrsrp"],
            sliders["f1_cov_a5threshold1rsrp"],
            "red",
        ),
        create_vertical_line(
            -7,
            sliders["a2criticalthresholdrsrp"],
            sliders["f1_iflb_a5threshold1rsrp"],
            "blue",
        ),
        create_vertical_line(
            9,
            -44,
            f1_threshxlow_map,
            "green",
        ),
        create_vertical_line(8, max_value, sliders["f1_cov_a5threshold2rsrp"], "red"),
        create_vertical_line(7, max_value, sliders["f1_iflb_a5threshold2rsrp"], "blue"),
    ]


def create_lines(
    sliders,
    f1_threshservinglow_map,
    f1_threshxlow_map,
    f1_snonintrasearch_map,
    max_value=-44,
):
    return [
        go.Scatter(
            x=[-12, -7],
            y=[
                sliders["f1_iflb_a5threshold1rsrp"],
                sliders["f1_iflb_a5threshold1rsrp"],
            ],
            mode="lines",
            line=dict(color="blue", dash="dot"),
        ),
        go.Scatter(
            x=[-12, -10],
            y=[
                f1_snonintrasearch_map,
                f1_snonintrasearch_map,
            ],
            mode="lines",
            line=dict(color="green", dash="dot"),
        ),
        go.Scatter(
            x=[-12, -9],
            y=[
                f1_threshservinglow_map,
                f1_threshservinglow_map,
            ],
            mode="lines",
            line=dict(color="green", dash="dot"),
        ),
        go.Scatter(
            x=[-12, -10],
            y=[
                sliders["f1_a1a2searchthresholdrsrp"],
                sliders["f1_a1a2searchthresholdrsrp"],
            ],
            mode="lines",
            line=dict(color="red", dash="dot"),
        ),
        go.Scatter(
            x=[-12, -8],
            y=[
                sliders["f1_cov_a5threshold1rsrp"],
                sliders["f1_cov_a5threshold1rsrp"],
            ],
            mode="lines",
            line=dict(color="red", dash="dot"),
        ),
        go.Scatter(
            x=[-12, -9],
            y=[
                sliders["qrxlevmin"],
                sliders["qrxlevmin"],
            ],
            mode="lines",
            line=dict(color="green", dash="dot"),
        ),
        go.Scatter(
            x=[-12, -8],
            y=[
                sliders["a2criticalthresholdrsrp"],
                sliders["a2criticalthresholdrsrp"],
            ],
            mode="lines",
            line=dict(color="red", dash="dot"),
        ),
        go.Scatter(
            x=[7, 7.5],
            y=[
                max_value,
                max_value,
            ],
            mode="lines",
            line=dict(color="blue", dash="dot"),
        ),
        go.Scatter(
            x=[8, 8.5],
            y=[
                max_value,
                max_value,
            ],
            mode="lines",
            line=dict(color="red", dash="dot"),
        ),
        go.Scatter(
            x=[9, 9.5],
            y=[
                max_value,
                max_value,
            ],
            mode="lines",
            line=dict(color="green", dash="dot"),
        ),
        go.Scatter(
            x=[9, 12],
            y=[
                f1_threshxlow_map,
                f1_threshxlow_map,
            ],
            mode="lines",
            line=dict(color="green", dash="dot"),
        ),
        go.Scatter(
            x=[8, 12],
            y=[
                sliders["f1_cov_a5threshold2rsrp"],
                sliders["f1_cov_a5threshold2rsrp"],
            ],
            mode="lines",
            line=dict(color="red", dash="dot"),
        ),
        go.Scatter(
            x=[7, 12],
            y=[
                sliders["f1_iflb_a5threshold2rsrp"],
                sliders["f1_iflb_a5threshold2rsrp"],
            ],
            mode="lines",
            line=dict(color="blue", dash="dot"),
        ),
        go.Scatter(
            x=[-8, 5],
            y=[
                sliders["a2criticalthresholdrsrp"],
                sliders["a2criticalthresholdrsrp"],
            ],
            mode="lines+markers+text",
            line=dict(color="red", shape="spline"),
            text=["", "A2 Critical HO"],
            textposition="bottom center",
            textfont=dict(color="red", size=15),
            marker=dict(symbol="arrow-bar-up", size=15, angleref="previous"),
        ),
        # go.Scatter(
        #     x=[-12, -9],
        #     y=[sliders["qrxlevmin"], sliders["qrxlevmin"]],
        #     mode="lines",
        #     line=dict(color="green", dash="dot"),
        # ),
        # go.Scatter(
        #     x=[-12, -10],
        #     y=[f1_snonintrasearch_map, f1_snonintrasearch_map],
        #     mode="lines",
        #     line=dict(color="green", dash="dot"),
        # ),
        # go.Scatter(
        #     x=[-12, -9],
        #     y=[f1_threshservinglow_map, f1_threshservinglow_map],
        #     mode="lines",
        #     line=dict(color="green", dash="dot"),
        # ),
        # go.Scatter(
        #     x=[-12, -7],
        #     y=[sliders["a2criticalthresholdrsrp"], sliders["a2criticalthresholdrsrp"]],
        #     mode="lines",
        #     line=dict(color="red", dash="dot"),
        # ),
        # go.Scatter(
        #     x=[-12, -8],
        #     y=[sliders["f1_cov_a5threshold1rsrp"], sliders["f1_cov_a5threshold1rsrp"]],
        #     mode="lines",
        #     line=dict(color="red", dash="dot"),
        # ),
        # go.Scatter(
        #     x=[-12, -10],
        #     y=[
        #         sliders["f1_a1a2searchthresholdrsrp"],
        #         sliders["f1_a1a2searchthresholdrsrp"],
        #     ],
        #     mode="lines",
        #     line=dict(color="red", dash="dot"),
        # ),
        # # go.Scatter(
        #     x=[-6, 2],
        #     y=[sliders["a2criticalthresholdrsrp"], sliders["a2criticalthresholdrsrp"]],
        #     mode="lines+text",
        #     line=dict(color="red", shape="spline"),
        #     text="A2 Critical HO",
        #     textposition="top center",
        #     textfont=dict(color="red", size=15),
        #     marker=dict(symbol="arrow", size=15, angleref="previous"),
        # ),
        # go.Scatter(
        #     x=[-18, -6, 6, 18],
        #     y=[
        #         ((sliders["qrxlevmin"] + max_value) / 1.5),
        #         ((sliders["qrxlevmin"] + max_value) / 1.5),
        #         ((f1_threshxhigh_map + max_value) / 2),
        #         ((f1_threshxhigh_map + max_value) / 2),
        #     ],
        #     line=dict(color="green", shape="spline", dash="dashdot"),
        #     marker=dict(symbol="arrow-bar-up", size=15, angleref="previous"),
        # ),
        # go.Scatter(
        #     x=[-12, -6, 6, 16],
        #     y=[
        #         (
        #             (
        #                 sliders["a2criticalthresholdrsrp"]
        #                 + sliders["f1_iflb_a5threshold1rsrp"]
        #             )
        #             / 1.5
        #         ),
        #         (
        #             (
        #                 sliders["a2criticalthresholdrsrp"]
        #                 + sliders["f1_iflb_a5threshold1rsrp"]
        #             )
        #             / 1.5
        #         ),
        #         (sliders["f1_iflb_a5threshold2rsrp"] - max_value / 2),
        #         (sliders["f1_iflb_a5threshold2rsrp"] - max_value / 2),
        #     ],
        #     line=dict(color="blue", shape="spline", dash="dashdot"),
        #     marker=dict(symbol="arrow-bar-up", size=15, angleref="previous"),
        # ),
        # go.Scatter(
        #     x=[16, 10, -2, -14],
        #     y=[
        #         (
        #             (
        #                 sliders["a2criticalthresholdrsrp"]
        #                 + sliders["f1_cov_a5threshold1rsrp"]
        #             )
        #             / 2
        #         ),
        #         (
        #             (
        #                 sliders["a2criticalthresholdrsrp"]
        #                 + sliders["f1_cov_a5threshold1rsrp"]
        #             )
        #             / 2
        #         ),
        #         ((sliders["f1_cov_a5threshold2rsrp"] + max_value) / 2),
        #         ((sliders["f1_cov_a5threshold2rsrp"] + max_value) / 2),
        #     ],
        #     line=dict(color="red", shape="spline", dash="dashdot"),
        #     marker=dict(symbol="arrow-bar-up", size=15, angleref="previous"),
        # ),
        # go.Scatter(
        #     x=[19, 10, -2, -16],
        #     y=[
        #         ((f1_threshservinglow_map + sliders["qrxlevmin"]) / 2),
        #         ((f1_threshservinglow_map + sliders["qrxlevmin"]) / 2),
        #         ((f1_threshxlow_map + max_value) / 2),
        #         ((f1_threshxlow_map + max_value) / 2),
        #     ],
        #     line=dict(color="green", shape="spline", dash="dashdot"),
        #     marker=dict(symbol="arrow-bar-up", size=15, angleref="previous"),
        # ),
        # go.Scatter(
        #     x=[18, 10, -2, -10],
        #     y=[
        #         (
        #             (
        #                 sliders["a2criticalthresholdrsrp"]
        #                 + sliders["f1_iflb_a5threshold1rsrp"]
        #             )
        #             / 2.2
        #         ),
        #         (
        #             (
        #                 sliders["a2criticalthresholdrsrp"]
        #                 + sliders["f1_iflb_a5threshold1rsrp"]
        #             )
        #             / 2.2
        #         ),
        #         ((sliders["f1_iflb_a5threshold2rsrp"] + max_value) / 2.5),
        #         ((sliders["f1_iflb_a5threshold2rsrp"] + max_value) / 2.5),
        #     ],
        #     line=dict(color="blue", shape="spline", dash="dashdot"),
        #     marker=dict(symbol="arrow-bar-up", size=15, angleref="previous"),
        # ),
    ]


def configure_plot(
    sliders,
    f1_threshservinglow_map,
    f1_threshxlow_map,
    f1_snonintrasearch_map,
    max_value,
):
    vertical_lines = create_vertical_lines(
        sliders,
        f1_threshservinglow_map,
        f1_threshxlow_map,
        max_value,
    )
    lines = create_lines(
        sliders,
        f1_threshservinglow_map,
        f1_threshxlow_map,
        f1_snonintrasearch_map,
        max_value,
    )

    fig = go.Figure(data=lines)
    bottom_range = sliders["a2criticalthresholdrsrp"] - 4
    fig.update_layout(
        shapes=vertical_lines,
        xaxis=dict(range=[-12, 12], showticklabels=False, showgrid=False),
        yaxis=dict(
            range=[bottom_range, max_value],
            showticklabels=False,
            showgrid=False,
            zeroline=False,
            showline=False,
        ),
        showlegend=False,
        height=700,
        margin=dict(
            autoexpand=False,
            l=300,
            r=300,
            t=100,
            b=100,
        ),
    )
    fig.add_vrect(
        x0=-12,
        x1=-10,
        fillcolor="grey",
        opacity=0.25,
        line_width=0,
    )
    fig.add_vrect(
        x0=10,
        x1=12,
        fillcolor="grey",
        opacity=0.25,
        line_width=0,
    )

    annotations = []

    # y_data_left = [
    #     sliders["a2criticalthresholdrsrp"],
    #     sliders["qrxlevmin"],
    #     sliders["f1_cov_a5threshold2rsrp"],
    #     sliders["f1_iflb_a5threshold2rsrp"],
    #     sliders["f1_iflb_a5threshold1rsrp"],
    # ]
    # y_data_right = [
    #     sliders["a2criticalthresholdrsrp"],
    #     sliders["qrxlevmin"],
    #     sliders["f1_cov_a5threshold1rsrp"],
    #     sliders["f1_a1a2searchthresholdrsrp"],
    #     sliders["f1_iflb_a5threshold2rsrp"],
    #     sliders["f1_iflb_a5threshold1rsrp"],
    # ]

    # labels_left = [
    #     "F1 A2ThresholdRSRP",
    #     "F1 QRxLevMin",
    #     "(set on F2) ThreshXLow",
    #     "(set on F2) COV A5Threshold2",
    #     "(set on F2) IFLB A5Threshold2",
    # ]

    # colors_left = ["blue", "blue", "green", "red", "blue"]

    # labels_right = [
    #     "F2 A2Threshold",
    #     "F2 QRxLevMin",
    #     "COV A5Threshold1",
    #     "A1A2 Threshold",
    #     "ThreshServingLow",
    #     "SNonIntraSearch",
    #     "(set on F1) IFLB A5Threshold2",
    #     "IFLB A5Threshold1",
    #     "(set on F1) ThreshXHigh",
    # ]
    # colors_right = [
    #     "red",
    #     "green",
    #     "red",
    #     "red",
    #     "green",
    #     "green",
    #     "blue",
    #     "blue",
    #     "green",
    # ]

    # max_len_left = len(y_data_left)
    # max_len_right = len(y_data_right)
    # max_len = max(max_len_left, max_len_right)

    # for i in range(max_len):
    #     if i < max_len_left:
    #         y_trace = y_data_left[i]
    #         label = labels_left[i]
    #         color = colors_left[i]
    #         annotations.append(
    #             dict(
    #                 x=-12,
    #                 y=y_trace,
    #                 xanchor="right",
    #                 yanchor="middle",
    #                 text=f"{label}:{y_trace}",
    #                 font=dict(family="Ericsson Hilda Light", size=12, color=color),
    #                 showarrow=False,
    #                 xref="x",
    #                 yref="y",
    #             )
    #         )
    #     if i < max_len_right:
    #         y_trace = y_data_right[i]
    #         label = labels_right[i]
    #         color = colors_right[i]
    #         annotations.append(
    #             dict(
    #                 x=12,
    #                 y=y_trace,
    #                 xanchor="left",
    #                 yanchor="middle",
    #                 text=f"{label}:{y_trace}",
    #                 font=dict(family="Ericsson Hilda Light", size=12, color=color),
    #                 showarrow=False,
    #                 xref="x",
    #                 yref="y",
    #             )
    #         )

    annotations.append(
        dict(
            xref="paper",
            yref="paper",
            x=-0.15,
            y=1.1,
            xanchor="left",
            yanchor="bottom",
            text="Mobility Actions and Thresholds for the Sticky Carrier Configuration",
            font=dict(family="Arial", size=30, color="rgb(37,37,37)"),
            showarrow=False,
        )
    )
    # Source

    fig.add_annotation(
        x=11,
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
        x=-11,
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
        x=11,
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
        x=-11,
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


def stylings(text, font_size=10, text_align="center"):
    style = f"""
    <style>
        .container {{
            width: 100%;
        }}
        .text {{
            font-size: {font_size}px;
            text-align: {text_align};
            line-height: 1.5; /* Adjust line height for space between lines */
        }}
    </style>
    <div class="container">
        <div class="text">
            {text}
        </div>
    </div>
    """
    return style


def run_sticky():
    columns = st.columns(11, gap="small")

    column_texts = [
        "F1<br>A2 Critical<br>&emsp;&emsp;&emsp;",
        "F1<br>QRxLevMin<br>SIB1",
        "F1<br>QRxLevMin<br>SIB3",
        "F1<br>sNonIntraSearch<br>&emsp;&emsp;&emsp;",
        "F1<br>threshServingLow<br>&emsp;&emsp;&emsp;",
        "F1<br>threshXLow<br>&emsp;&emsp;&emsp;",
        "F1<br>A1A2 SearchThreshold<br>&emsp;&emsp;&emsp;",
        "F1<br>COV<br>A5Threshold1",
        "F1<br>COV<br>A5Threshold2",
        "F1<br>IFLB<br>A5Threshold1",
        "F1<br>IFLB<br>A5Threshold2",
    ]

    for column, text in zip(columns, column_texts):
        with column.container():
            st.markdown(stylings(text), unsafe_allow_html=True)

    container = st.container()
    with container:
        sliders = configure_sliders(columns)

    (
        f1_threshservinglow_map,
        f1_threshxlow_map,
        f1_snonintrasearch_map,
        max_value,
    ) = compute_threshold_mappings(sliders)
    fig = configure_plot(
        sliders,
        f1_threshservinglow_map,
        f1_threshxlow_map,
        f1_snonintrasearch_map,
        max_value,
    )

    col1, col2 = st.columns([3, 1.5])
    with col1:
        with stylable_container(
            key="container_with_border",
            css_styles="""
                {
                    background-color: #FFFFFF;
                    border: 2px solid rgba(49, 51, 63, 0.2);
                    border-radius: 0.5rem;
                    padding: calc(1em - 1px)
                }
                """,
        ):
            container = st.container()
            with container:
                st.plotly_chart(fig, use_container_width=True)
    with col2:
        with stylable_container(
            key="container_with_border",
            css_styles="""
                {
                    background-color: #F8F9FB;
                    border: 2px solid rgba(49, 51, 63, 0.2);
                    font-size: 8px;
                    border-radius: 0.5rem;
                    padding: calc(1em - 1px)
                }
                """,
        ):
            con1 = st.container()
            with con1:
                generated_script = generate_scripts(sliders)
                st.code(generated_script, language="markdown")

        container = st.container()
        with container:
            st.markdown(
                multi_color_styling(
                    [
                        ("Green : idle mode", "green"),
                        (
                            "Red : connected mode<br>&emsp;&emsp;&emsp;coverage triggered",
                            "red",
                        ),
                        (
                            "Blue : connected mode<br>&emsp;&emsp;&emsp;IFLB triggered",
                            "blue",
                        ),
                    ]
                ),
                unsafe_allow_html=True,
            )
    st.markdown(
        """
        ### ✨ Sticky Carrier Configuration

        **Conclusion:**
        The article discusses mobility actions and relevant thresholds for configuring UE reselection and handover between frequencies F1 and F2. It highlights that the configuration is symmetric and explains the actions in both idle and connected modes.

        1. **Idle Mode Actions:**
            - A UE camped on F1 measures other frequencies when the serving RSRP drops below `sNonIntraSearch`.
            - Reselection to F2 occurs if F1 RSRP falls below `threshServingLow` and F2 RSRP is above `threshXLow`.
            - Above `threshServingLow`, the UE remains on F1 regardless of F2's strength.

        2. **Connected Mode Actions - Coverage Triggered:**
            - Triggered by the feature Mobility Control at Poor Coverage using `EVENT_A5`.
            - Handover to F2 occurs when F1 RSRP falls to `a5Threshold1Rsrp` and F2 RSRP is above `a5Threshold2Rsrp`.
            - Blind release-with-redirect can be triggered at `a2CriticalThresholdRsrp` if no suitable target is found.

        3. **Connected Mode Actions - IFLB:**
            - IFLB from F1 to F2 occurs when F1 RSRP is below `a5Threshold1Rsrp` (set to -44 dBm for IFLB) and F2 RSRP is above `a5Threshold2Rsrp`.
            - `a5Threshold2Rsrp` is typically set at or above `threshServingLow` to avoid immediate reselection to F1 in idle mode.

        These mobility actions ensure efficient UE reselection and handover, maintaining connectivity and load balancing between cells.

        <span style="color:red"><strong>Nb:</strong> MCPC must be active.
        """,
        unsafe_allow_html=True,
    )
