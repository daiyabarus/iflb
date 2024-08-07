import plotly.graph_objs as go
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_vertical_slider import vertical_slider as svs

from layout.styles import multi_color_styling


def create_slider(col, slider_config):
    with col:
        return svs(
            key=slider_config["key"],
            step=slider_config["step"],
            min_value=slider_config["min_value"],
            max_value=slider_config["max_value"],
            default_value=slider_config["default_value"],
            slider_color=slider_config["slider_color"],
            track_color=slider_config["track_color"],
            thumb_color=slider_config["thumb_color"],
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
    slider_configs = [
        {
            "key": "a2criticalthresholdrsrp",
            "step": 1,
            "min_value": -140,
            "max_value": -44,
            "default_value": -126,
            "slider_color": "#AAE89F",
            "track_color": "lightgrey",
            "thumb_color": "#5DC93E",
        },
        {
            "key": "qrxlevminsib3",
            "step": 1,
            "min_value": -140,
            "max_value": -44,
            "default_value": -124,
            "slider_color": "#AAE89F",
            "track_color": "lightgrey",
            "thumb_color": "#5DC93E",
        },
        {
            "key": "qrxlevminsib1",
            "step": 1,
            "min_value": -140,
            "max_value": -44,
            "default_value": -124,
            "slider_color": "#AAE89F",
            "track_color": "lightgrey",
            "thumb_color": "#5DC93E",
        },
        {
            "key": "f1_threshxhigh",
            "step": 1,
            "min_value": 0,
            "max_value": 62,
            "default_value": 28,
            "slider_color": "#008000",
            "track_color": "lightgray",
            "thumb_color": "#F1C40F",
        },
        {
            "key": "f1_iflb_a5threshold1rsrp",
            "step": 1,
            "min_value": -140,
            "max_value": -44,
            "default_value": -50,
            "slider_color": "#0000FF",
            "track_color": "lightgray",
            "thumb_color": "#F1C40F",
        },
        {
            "key": "f1_iflb_a5threshold2rsrp",
            "step": 1,
            "min_value": -140,
            "max_value": -44,
            "default_value": -96,
            "slider_color": "#0000FF",
            "track_color": "lightgray",
            "thumb_color": "#F1C40F",
        },
        {
            "key": "f2_threshservinglow",
            "step": 1,
            "min_value": 0,
            "max_value": 62,
            "default_value": 6,
            "slider_color": "#008000",
            "track_color": "lightgray",
            "thumb_color": "#C1392B",
        },
        {
            "key": "f2_threshxlow",
            "step": 1,
            "min_value": 0,
            "max_value": 62,
            "default_value": 4,
            "slider_color": "#008000",
            "track_color": "lightgray",
            "thumb_color": "#C1392B",
        },
        {
            "key": "f2_snonintrasearch",
            "step": 1,
            "min_value": 0,
            "max_value": 62,
            "default_value": 8,
            "slider_color": "#008000",
            "track_color": "lightgray",
            "thumb_color": "#C1392B",
        },
        {
            "key": "f2_a1a2searchthresholdrsrp",
            "step": 1,
            "min_value": -140,
            "max_value": -44,
            "default_value": -110,
            "slider_color": "#FA0101",
            "track_color": "lightgray",
            "thumb_color": "#C1392B",
        },
        {
            "key": "f2_cov_a5threshold1rsrp",
            "step": 1,
            "min_value": -140,
            "max_value": -44,
            "default_value": -113,
            "slider_color": "#FA0101",
            "track_color": "lightgray",
            "thumb_color": "#C1392B",
        },
        {
            "key": "f2_cov_a5threshold2rsrp",
            "step": 1,
            "min_value": -140,
            "max_value": -44,
            "default_value": -106,
            "slider_color": "#FA0101",
            "track_color": "lightgray",
            "thumb_color": "#C1392B",
        },
        {
            "key": "f2_iflb_a5threshold1rsrp",
            "step": 1,
            "min_value": -140,
            "max_value": -44,
            "default_value": -72,
            "slider_color": "#0000FF",
            "track_color": "lightgray",
            "thumb_color": "#C1392B",
        },
        {
            "key": "f2_iflb_a5threshold2rsrp",
            "step": 1,
            "min_value": -140,
            "max_value": -44,
            "default_value": -90,
            "slider_color": "#0000FF",
            "track_color": "lightgray",
            "thumb_color": "#C1392B",
        },
    ]

    sliders = {}
    for i, config in enumerate(slider_configs):
        sliders[config["key"]] = create_slider(columns[i], config)

    return sliders


def generate_scripts(sliders):
    script_lines = [
        "# SET ON F1",
        f'set `F1` A2Critical {sliders["a2criticalthresholdrsrp"]} dBm',
        f'set `F1` QRxLevMin {sliders["qrxlevminsib1"]} dBm ',
        f'set `F1` EUtranFreq `F2` qRxLevMin {sliders["qrxlevminsib3"]} dBm',
        f'set `F1` EUtranFreq `F2` threshXHigh {sliders["f1_threshxhigh"]} dB',
        f'set `F1` IFLB A5Threshold1 {sliders["f1_iflb_a5threshold1rsrp"]} dBm',
        f'set `F1` IFLB A5Threshold2 {sliders["f1_iflb_a5threshold2rsrp"]} dBm',
        "",
        "# SET ON F2",
        f'set `F2` A2Critical {sliders["a2criticalthresholdrsrp"]} dBm',
        f'set `F2` qRxLevMin {sliders["qrxlevminsib1"]} dB',
        f'set `F2` EUtranFreq `F1` qRxLevMin {sliders["qrxlevminsib3"]} dBm',
        f'set `F2` threshServingLow {sliders["f2_threshservinglow"]} dB',
        f'set `F2` EUtranFreq `F1` threshXLow {sliders["f2_threshxlow"]} dB',
        f'set `F2` SIB3 sNonIntraSearch {sliders["f2_snonintrasearch"]} dB',
        f'set `F2` A1A2 SearchThreshold RSRP {sliders["f2_a1a2searchthresholdrsrp"]} dBm',
        f'set `F2` COV A5Threshold1 {sliders["f2_cov_a5threshold1rsrp"]} dBm',
        f'set `F2` COV A5Threshold2 {sliders["f2_cov_a5threshold2rsrp"]} dBm',
        f'set `F2` IFLB A5Threshold1 {sliders["f2_iflb_a5threshold1rsrp"]} dBm',
        f'set `F2` IFLB A5Threshold2 {sliders["f2_iflb_a5threshold2rsrp"]} dBm',
    ]

    script = "\n".join(script_lines)
    return script


def compute_threshold_mappings(sliders):
    MAX_VALUE = -44

    def compute_value(threshold, critical_threshold, factor):
        if threshold <= MAX_VALUE and threshold > critical_threshold:
            return threshold + ((critical_threshold - threshold) / factor)
        return threshold

    f1_threshxhigh_map = (sliders["f1_threshxhigh"] * 2) + sliders["qrxlevminsib3"]
    f2_threshservinglow_map = (sliders["f2_threshservinglow"] * 2) + sliders[
        "qrxlevminsib1"
    ]
    f2_threshxlow_map = (sliders["f2_threshxlow"] * 2) + sliders["qrxlevminsib3"]
    f2_snonintrasearch_map = (sliders["f2_snonintrasearch"] * 2) + sliders[
        "qrxlevminsib1"
    ]
    green_left = int(compute_value(MAX_VALUE, sliders["qrxlevminsib3"], 6.5))
    green_right = int(compute_value(MAX_VALUE, f1_threshxhigh_map, 2))

    green_left1 = int(compute_value(MAX_VALUE, f2_threshxlow_map, 1.4))
    green_right1 = int(
        compute_value(f2_threshservinglow_map, sliders["qrxlevminsib3"], 5)
    )

    red_left = int(compute_value(MAX_VALUE, sliders["f2_cov_a5threshold2rsrp"], 1.1))
    red_right = int(
        compute_value(
            sliders["f2_cov_a5threshold1rsrp"], sliders["a2criticalthresholdrsrp"], 2
        )
    )

    blue_left = int(
        compute_value(
            sliders["f1_iflb_a5threshold1rsrp"], sliders["a2criticalthresholdrsrp"], 6.5
        )
    )
    blue_right = int(compute_value(MAX_VALUE, sliders["f1_iflb_a5threshold2rsrp"], 3))

    blue_left1 = int(compute_value(MAX_VALUE, sliders["f2_iflb_a5threshold2rsrp"], 1.2))
    blue_right1 = int(
        compute_value(
            sliders["f2_iflb_a5threshold1rsrp"], sliders["a2criticalthresholdrsrp"], 5
        )
    )

    return {
        "f1_threshxhigh_map": f1_threshxhigh_map,
        "f2_threshservinglow_map": f2_threshservinglow_map,
        "f2_threshxlow_map": f2_threshxlow_map,
        "f2_snonintrasearch_map": f2_snonintrasearch_map,
        "MAX_VALUE": MAX_VALUE,
        "blue_left": blue_left,
        "blue_right": blue_right,
        "blue_left1": blue_left1,
        "blue_right1": blue_right1,
        "green_left": green_left,
        "green_right": green_right,
        "green_left1": green_left1,
        "green_right1": green_right1,
        "red_left": red_left,
        "red_right": red_right,
    }


# TODOS : Update Vertical Line
def create_vertical_lines(sliders, mappings):
    return [
        create_vertical_line(
            -9, sliders["qrxlevminsib1"], mappings["MAX_VALUE"], "green"
        ),
        create_vertical_line(
            -8, mappings["f2_threshxlow_map"], mappings["MAX_VALUE"], "green"
        ),
        create_vertical_line(
            -7, sliders["f2_cov_a5threshold2rsrp"], mappings["MAX_VALUE"], "red"
        ),
        create_vertical_line(
            -6,
            sliders["a2criticalthresholdrsrp"],
            sliders["f1_iflb_a5threshold1rsrp"],
            "blue",
        ),
        create_vertical_line(
            -5, sliders["f2_iflb_a5threshold2rsrp"], mappings["MAX_VALUE"], "blue"
        ),
        create_vertical_line(
            9, mappings["f1_threshxhigh_map"], mappings["MAX_VALUE"], "green"
        ),
        create_vertical_line(
            9,
            sliders["f2_iflb_a5threshold1rsrp"],
            sliders["a2criticalthresholdrsrp"],
            "blue",
        ),
        create_vertical_line(
            8.5, sliders["qrxlevminsib1"], mappings["f2_threshservinglow_map"], "green"
        ),
        create_vertical_line(
            8,
            sliders["a2criticalthresholdrsrp"],
            sliders["f2_cov_a5threshold1rsrp"],
            "red",
        ),
        create_vertical_line(
            8, sliders["f1_iflb_a5threshold2rsrp"], mappings["MAX_VALUE"], "blue"
        ),
    ]


def create_lines(sliders, mappings):
    return (
        create_threshold_lines(sliders, mappings)
        + create_legend_lines()
        + create_critical_handover_line(sliders)
        + create_splines(mappings)
    )


# TODOs : Update Horizontal line
def create_threshold_lines(sliders, mappings):
    threshold_configs = [
        ([-12, -5], sliders["f2_iflb_a5threshold2rsrp"], "blue"),
        ([-12, -6], sliders["f1_iflb_a5threshold1rsrp"], "blue"),
        ([-12, -6], sliders["a2criticalthresholdrsrp"], "red"),
        ([-12, -7], sliders["f2_cov_a5threshold2rsrp"], "red"),
        ([-12, -8], mappings["f2_threshxlow_map"], "green"),
        ([-12, -9], sliders["qrxlevminsib3"], "green"),
        ([9, 12], sliders["f2_iflb_a5threshold1rsrp"], "blue"),
        ([9, 12], mappings["f1_threshxhigh_map"], "green"),
        ([10, 12], mappings["f2_snonintrasearch_map"], "green"),
        ([9.5, 12], sliders["f2_a1a2searchthresholdrsrp"], "red"),
        ([8.5, 12], sliders["qrxlevminsib3"], "green"),
        ([8.5, 12], mappings["f2_threshservinglow_map"], "green"),
        ([8, 12], sliders["a2criticalthresholdrsrp"], "red"),
        ([8, 12], sliders["f2_cov_a5threshold1rsrp"], "red"),
        ([8, 12], sliders["f1_iflb_a5threshold2rsrp"], "blue"),
    ]
    return [create_threshold_line(x, y, color) for x, y, color in threshold_configs]


def create_threshold_line(x, y, color):
    return go.Scatter(
        x=x,
        y=[y, y],
        mode="lines",
        line=dict(color=color, dash="dot"),
    )


def create_legend_lines():
    legend_configs = [
        ([-9.5, -9], -44, "green"),
        ([-8.5, -8], -44, "green"),
        ([-7.5, -7], -44, "red"),
        ([-5.5, -5], -44, "blue"),
        ([8, 8.5], -44, "blue"),
        ([9, 9.5], -44, "green"),
    ]
    return [create_threshold_line(x, y, color) for x, y, color in legend_configs]


def create_critical_handover_line(sliders):
    return [
        go.Scatter(
            x=[7.5, 0, -2.5, -5],
            y=[sliders["a2criticalthresholdrsrp"]] * 4,
            mode="lines+markers+text",
            line=dict(color="red", shape="spline"),
            text=["", "", "A2 Critical HO", ""],
            textposition="top center",
            textfont=dict(color="red", size=15),
            marker=dict(
                symbol=[
                    "circle",
                    "circle",
                    "circle",
                    "arrow-bar-up",
                ],
                size=[15, 0, 0, 15],
                angleref="previous",
            ),
        )
    ]


# TODOS :try to remove redundancy
def create_splines(mappings):
    splines = []
    directions = ["right", "left"]
    for direction in directions:
        if direction == "right":
            spline_configs = [
                ("blue", mappings["blue_right1"], mappings["blue_left1"]),
                ("green", mappings["green_right1"], mappings["green_left1"]),
                ("red", mappings["red_right"], mappings["red_left"]),
            ]
        else:
            spline_configs = [
                ("blue", mappings["blue_left"], mappings["blue_right"]),
                ("green", mappings["green_left"], mappings["green_right"]),
            ]

        for color, first, second in spline_configs:
            splines.append(create_spline_line(color, first, second, direction))
    return splines


def create_spline_line(color, first, second, direction):
    x_values = get_x_values(color, direction)
    y_values = [first, first, second, second]
    marker_symbols = get_marker_symbols(color)

    return go.Scatter(
        x=x_values,
        y=y_values,
        line=dict(color=color, dash="dashdot"),
        mode="lines+markers",
        marker=dict(
            symbol=marker_symbols,
            size=[10, 0, 0, 15],
            color=color,
            angleref="previous",
        ),
    )


def get_x_values(color, direction):
    values = {
        "left": {
            "green": [-9, -2, -2, 9],
            "blue": [-6, -3.5, -3.5, 8],
        },
        "right": {
            "green": [8.5, 3, 3, -8],
            "blue": [9, 4, 4, -5],
            "red": [8, -2, -2, -7],
        },
    }
    return values[direction][color]


def get_marker_symbols(color):
    default_symbols = ["circle", "circle", "circle", "arrow-bar-up"]
    return ["y-right"] + default_symbols[1:] if color == "red" else default_symbols


# TODOS  END


def configure_plot(sliders, mappings):
    fig = create_base_figure(sliders, mappings)
    add_background_rectangles(fig)
    add_all_annotations(fig, sliders, mappings)
    return fig


def create_base_figure(sliders, mappings):
    fig = go.Figure(data=create_lines(sliders, mappings))
    bottom_range = sliders["a2criticalthresholdrsrp"] - 4
    fig.update_layout(
        shapes=create_vertical_lines(sliders, mappings),
        xaxis=dict(range=[-12, 12], showticklabels=False, showgrid=False),
        yaxis=dict(
            range=[bottom_range, (mappings["MAX_VALUE"] + 4)],
            showticklabels=False,
            showgrid=False,
            zeroline=False,
            showline=False,
        ),
        showlegend=False,
        height=700,
        margin=dict(autoexpand=False, l=300, r=300, t=100, b=100),
    )
    return fig


def add_background_rectangles(fig):
    for x0, x1 in [(-12, -10), (10, 12)]:
        fig.add_vrect(x0=x0, x1=x1, fillcolor="grey", opacity=0.25, line_width=0)


def add_all_annotations(fig, sliders, mappings):
    add_threshold_annotations(fig, sliders, mappings)
    add_title_annotation(fig)
    add_cell_annotations(fig)
    add_spline_annotations(fig, mappings)


def add_threshold_annotations(fig, sliders, mappings):
    LEFT_X_POS, RIGHT_X_POS = -0.01, 1
    left_annotations = [
        (
            sliders["a2criticalthresholdrsrp"],
            f"A2 Critical: {sliders['a2criticalthresholdrsrp']}",
            "red",
        ),
        (
            sliders["qrxlevminsib3"],
            f"QRxlevminSIB3: {sliders['qrxlevminsib3']}",
            "green",
        ),
        (
            mappings["f2_threshxlow_map"],
            f"(Set on F2 Cell)<br>ThreshXLow: {sliders['f2_threshxlow']}",
            "green",
        ),
        (
            sliders["f2_cov_a5threshold2rsrp"],
            f"(Set on F2 Cell)<br>COV A5Threshold2: {sliders['f2_cov_a5threshold2rsrp']}",
            "red",
        ),
        (
            sliders["f2_iflb_a5threshold2rsrp"],
            f"(Set on F2 Cell)<br>IFLB A5Threshold2: {sliders['f2_iflb_a5threshold2rsrp']}",
            "blue",
        ),
        (
            sliders["f1_iflb_a5threshold1rsrp"],
            f"IFLB A5Threshold1: {sliders['f1_iflb_a5threshold1rsrp']}",
            "blue",
        ),
    ]
    right_annotations = [
        (
            sliders["a2criticalthresholdrsrp"],
            f"A2 Critical: {sliders['a2criticalthresholdrsrp']}",
            "red",
        ),
        (
            sliders["qrxlevminsib3"],
            f"QRxlevminSIB3: {sliders['qrxlevminsib3']}",
            "green",
        ),
        (
            sliders["f2_cov_a5threshold1rsrp"],
            f"COV A5Threshold1: {sliders['f2_cov_a5threshold1rsrp']}",
            "red",
        ),
        (
            sliders["f2_a1a2searchthresholdrsrp"],
            f"A1A2Threshold: {sliders['f2_a1a2searchthresholdrsrp']}",
            "red",
        ),
        (
            mappings["f2_threshservinglow_map"],
            f"ThreshServingLow: {sliders['f2_threshservinglow']}",
            "green",
        ),
        (
            mappings["f2_snonintrasearch_map"],
            f"SNonIntraSearch: {sliders['f2_snonintrasearch']}",
            "green",
        ),
        (
            sliders["f1_iflb_a5threshold2rsrp"],
            f"(Set on F1 Cell)<br>IFLB A5Threshold2: {sliders['f1_iflb_a5threshold2rsrp']}",
            "blue",
        ),
        (
            sliders["f2_iflb_a5threshold1rsrp"],
            f"IFLB A5Threshold1: {sliders['f2_iflb_a5threshold1rsrp']}",
            "blue",
        ),
        (
            mappings["f1_threshxhigh_map"],
            f"(Set on F1 Cell) ThreshXHigh: {sliders['f1_threshxhigh']}",
            "green",
        ),
    ]

    for y, label, color in left_annotations:
        fig.add_annotation(
            x=LEFT_X_POS,
            y=y,
            xref="paper",
            text=label,
            showarrow=False,
            font=dict(family="Ericsson Hilda Light", size=12, color=color),
            xanchor="right",
            yanchor="middle",
        )

    for y, label, color in right_annotations:
        fig.add_annotation(
            x=RIGHT_X_POS,
            y=y,
            xref="paper",
            text=label,
            showarrow=False,
            font=dict(family="Ericsson Hilda Light", size=12, color=color),
            xanchor="left",
            yanchor="middle",
        )


def add_title_annotation(fig):
    fig.add_annotation(
        xref="paper",
        yref="paper",
        x=-0.23,
        y=1.1,
        xanchor="left",
        yanchor="bottom",
        text="Mobility Actions and Thresholds for the Priority Carrier Configuration",
        font=dict(family="Arial", size=30, color="rgb(37,37,37)"),
        showarrow=False,
    )


def add_spline_annotations(fig, mappings):
    annotations = [
        ("blue_left1", "blue", "A5 IFLB HO"),
        ("red_right", "red", "A5 COVERAGE HO"),
        ("green_right", "green", "Reselect<br>higher priority"),
        ("green_right1", "green", "Reselect<br>lower priority"),
    ]

    for y_pos_key, color, text in annotations:
        y_value = mappings[y_pos_key]
        fig.add_annotation(
            x=1,
            y=y_value,
            text=text,
            showarrow=False,
            font=dict(size=14, family="Ericsson Hilda Light", color=color),
            xref="x",
            yref="y",
            xanchor="center",
            yanchor="bottom",
        )


def add_cell_annotations(fig):
    cell_annotations = [
        (11, 1, "F2 Cell<br>Higher Prio", "bottom"),
        (-11, 1, "F1 Cell<br>Lower Prio", "bottom"),
        (11, -0.01, "🔻<br>Lowest<br>RSRP", "top"),
        (-11, -0.01, "🔻<br>Lowest<br>RSRP", "top"),
    ]
    for x, y, text, yanchor in cell_annotations:
        fig.add_annotation(
            x=x,
            y=y,
            text=text,
            showarrow=False,
            font=dict(size=14, family="Ericsson Hilda Light", color="rgb(150,150,150)"),
            xref="x",
            yref="paper",
            xanchor="center",
            yanchor=yanchor,
        )


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


def run_priority():
    columns = st.columns(14, gap="small")

    column_texts = [
        "F1 & F2<br>A2 Critical<br>&emsp;&emsp;&emsp;",
        "F1 & F2<br>QRxLevMin<br>SIB1",
        "F1 & F2<br>QRxLevMin<br>SIB3",
        "F1<br>ThreshXHigh<br>&emsp;&emsp;&emsp;",
        "F1<br>IFLB<br>A5Threshold1RSRP",
        "F1<br>IFLB<br>A5Threshold2RSRP",
        "F2<br>ThreshServingLow<br>&emsp;&emsp;&emsp;",
        "F2<br>ThreshXLow<br>&emsp;&emsp;&emsp;",
        "F2<br>SNonIntraSearch<br>&emsp;&emsp;&emsp;",
        "F2<br>A1A2 Search<br>&emsp;&emsp;&emsp;",
        "F2<br>COV<br>A5Threshold1RSRP",
        "F2<br>COV<br>a5Threshold2RSRP",
        "F2<br>IFLB<br>A5Threshold1RSRP",
        "F2<br>IFLB<br>a5Threshold2RSRP",
    ]

    for column, text in zip(columns, column_texts):
        with column.container():
            st.markdown(stylings(text), unsafe_allow_html=True)

    container = st.container()
    with container:
        sliders = configure_sliders(columns)

    mappings = compute_threshold_mappings(sliders)
    fig = configure_plot(sliders, mappings)

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
    <div class="section">
        <h2>✨ Priority Carrier Configuration</h2>
        <div class="key-takeaways">
            <h3>Key Takeaways:</h3>
            <ul>
                <li>This configuration is typically used when carriers have vastly different coverage areas, such as low band vs. high band or macro cells vs. small cells.</li>
                <li>One carrier is assigned a higher idle mode priority via the `cellReselectionPriority` parameter.</li>
                <li>The configuration divides the signal strength plane into three regions (blue, green, and grey) based on key parameters: `threshXHigh`, `threshServingLow`, and `threshXLow`.</li>
                <li>It provides better control over UE distribution compared to Equal Priority or Sticky Carrier Configurations, balancing between actively pushing UEs to the high-priority carrier and leaving room for Inter-Frequency Load Balancing (IFLB).</li>
                <li>The configuration allows for fine-tuning of both idle mode behavior and connected mode actions, including coverage-triggered handovers and IFLB.</li>
                <li>Careful parameter setting is crucial to ensure that idle mode behavior, coverage fallback, and IFLB work harmoniously.</li>
            </ul>
        </div>
        <div class="conclusion">
            <h3>Conclusion:</h3>
            <p>The Priority Carrier Configuration offers a powerful approach to managing UE distribution across multiple frequency carriers with different coverage characteristics. It is particularly effective in scenarios where one carrier needs to be prioritized to maximize its utilization, while still maintaining overall network efficiency and coverage. The configuration allows network operators to strike a balance between actively pushing UEs to a preferred carrier in idle mode and allowing IFLB to distribute traffic in connected mode. By carefully adjusting parameters such as `threshXHigh`, `threshServingLow`, and various IFLB thresholds, operators can optimize network performance, maximize the use of all available carriers, and ensure seamless coverage transitions. However, implementing this configuration requires careful planning and ongoing optimization. Network operators must consider the specific characteristics of their network, including coverage patterns, capacity requirements, and user behavior, to determine the optimal settings for their particular scenario.</p>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        1. **Idle Mode Actions:**
            - **Reselection from F1 to F2:** Triggered when F2 RSRP exceeds `threshXHigh`.
            - **Reselection from F2 to F1:** Triggered when F2 RSRP falls below `threshServingLow` and F1 RSRP is above `threshXLow`.

        2. **Connected Mode Actions - Coverage Triggered:**
            - **Event A5 Handover from F2 to F1:** Triggered when F2 RSRP falls to `A1A2SearchThreshold` and `A5Threshold1`, and F1 RSRP is above `A5Threshold2`.
            - **Critical Release:** Triggered at `A2CriticalThreshold`.

        3. **Connected Mode Actions - IFLB:**
            - **IFLB from F1 to F2:** Triggered when F1 RSRP is below `A5Threshold1` and F2 RSRP is above `A5Threshold2`.
        """
    )
