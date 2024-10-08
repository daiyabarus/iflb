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
            "default_value": -123,
            "slider_color": "#AAE89F",
            "track_color": "lightgrey",
            "thumb_color": "#5DC93E",
        },
        {
            "key": "qrxlevminsib1",
            "step": 2,
            "min_value": -140,
            "max_value": -44,
            "default_value": -124,
            "slider_color": "#AAE89F",
            "track_color": "lightgrey",
            "thumb_color": "#5DC93E",
        },
        {
            "key": "qrxlevminsib3",
            "step": 2,
            "min_value": -140,
            "max_value": -44,
            "default_value": -120,
            "slider_color": "#AAE89F",
            "track_color": "lightgrey",
            "thumb_color": "#5DC93E",
        },
        {
            "key": "f1_snonintrasearch",
            "step": 2,
            "min_value": 0,
            "max_value": 62,
            "default_value": 12,
            "slider_color": "#AAE89F",
            "track_color": "lightgrey",
            "thumb_color": "#5DC93E",
        },
        {
            "key": "f1_threshservinglow",
            "step": 2,
            "min_value": 0,
            "max_value": 62,
            "default_value": 8,
            "slider_color": "#AAE89F",
            "track_color": "lightgrey",
            "thumb_color": "#5DC93E",
        },
        {
            "key": "f1_threshxlow",
            "step": 2,
            "min_value": 0,
            "max_value": 62,
            "default_value": 8,
            "slider_color": "#AAE89F",
            "track_color": "lightgrey",
            "thumb_color": "#5DC93E",
        },
        {
            "key": "f1_a1a2searchthresholdrsrp",
            "step": 1,
            "min_value": -140,
            "max_value": -44,
            "default_value": -110,
            "slider_color": "#FA0101",
            "track_color": "lightgray",
            "thumb_color": "#C1392B",
        },
        {
            "key": "f1_cov_a5threshold1rsrp",
            "step": 1,
            "min_value": -140,
            "max_value": -44,
            "default_value": -113,
            "slider_color": "#FA0101",
            "track_color": "lightgray",
            "thumb_color": "#C1392B",
        },
        {
            "key": "f1_cov_a5threshold2rsrp",
            "step": 1,
            "min_value": -140,
            "max_value": -44,
            "default_value": -108,
            "slider_color": "#FA0101",
            "track_color": "lightgray",
            "thumb_color": "#C1392B",
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
            "default_value": -100,
            "slider_color": "#0000FF",
            "track_color": "lightgray",
            "thumb_color": "#F1C40F",
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
        f'set `F1` QRxLevMin SIB1 {sliders["qrxlevminsib1"]} dBm ',
        f'set `F1` QRxLevMin SIB3 {sliders["qrxlevminsib3"]} dBm ',
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
    MAX_VALUE = -44

    def compute_value(threshold, critical_threshold, factor):
        if threshold <= MAX_VALUE and threshold > critical_threshold:
            return threshold + ((critical_threshold - threshold) / factor)
        return threshold

    f1_threshservinglow_map = (sliders["f1_threshservinglow"] * 2) + sliders[
        "qrxlevminsib3"
    ]
    f1_threshxlow_map = (sliders["f1_threshxlow"] * 2) + sliders["qrxlevminsib3"]
    f1_snonintrasearch_map = (sliders["f1_snonintrasearch"] * 2) + sliders[
        "qrxlevminsib3"
    ]

    blue_left = int(
        compute_value(
            sliders["f1_iflb_a5threshold1rsrp"], sliders["a2criticalthresholdrsrp"], 1.2
        )
    )
    blue_right = int(compute_value(-44, sliders["f1_iflb_a5threshold2rsrp"], 4))
    green_left = int(
        compute_value(f1_threshservinglow_map, sliders["qrxlevminsib3"], 2)
    )
    green_right = int(compute_value(-44, f1_threshxlow_map, 3))
    red_left = int(
        compute_value(
            sliders["f1_cov_a5threshold1rsrp"], sliders["a2criticalthresholdrsrp"], 2
        )
    )
    red_right = int(compute_value(-44, sliders["f1_cov_a5threshold2rsrp"], 2.5))

    return {
        "f1_threshservinglow_map": f1_threshservinglow_map,
        "f1_threshxlow_map": f1_threshxlow_map,
        "f1_snonintrasearch_map": f1_snonintrasearch_map,
        "MAX_VALUE": MAX_VALUE,
        "blue_left": blue_left,
        "blue_right": blue_right,
        "green_left": green_left,
        "green_right": green_right,
        "red_left": red_left,
        "red_right": red_right,
    }


def create_vertical_lines(sliders, mappings):
    return [
        create_vertical_line(-9, -140, sliders["qrxlevminsib3"]),
        create_vertical_line(
            -9, sliders["qrxlevminsib3"], mappings["f1_threshservinglow_map"], "green"
        ),
        create_vertical_line(-9, -140, mappings["f1_threshservinglow_map"]),
        create_vertical_line(
            -9, mappings["f1_threshservinglow_map"], sliders["qrxlevminsib1"], "green"
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
            9, mappings["MAX_VALUE"], mappings["f1_threshxlow_map"], "green"
        ),
        create_vertical_line(
            8, mappings["MAX_VALUE"], sliders["f1_cov_a5threshold2rsrp"], "red"
        ),
        create_vertical_line(
            7, mappings["MAX_VALUE"], sliders["f1_iflb_a5threshold2rsrp"], "blue"
        ),
    ]


def create_lines(sliders, mappings):
    return (
        create_threshold_lines(sliders, mappings)
        + create_legend_lines()
        + create_critical_handover_line(sliders)
        + create_spline_lines(mappings)
    )


def create_threshold_lines(sliders, mappings):
    threshold_configs = [
        ([-12, -7], sliders["f1_iflb_a5threshold1rsrp"], "blue"),
        ([-12, -10], mappings["f1_snonintrasearch_map"], "green"),
        ([-12, -9], mappings["f1_threshservinglow_map"], "green"),
        ([-12, -10], sliders["f1_a1a2searchthresholdrsrp"], "red"),
        ([-12, -8], sliders["f1_cov_a5threshold1rsrp"], "red"),
        ([-12, -9], sliders["qrxlevminsib1"], "green"),
        ([-12, -8], sliders["a2criticalthresholdrsrp"], "red"),
        ([9, 12], mappings["f1_threshxlow_map"], "green"),
        ([8, 12], sliders["f1_cov_a5threshold2rsrp"], "red"),
        ([7, 12], sliders["f1_iflb_a5threshold2rsrp"], "blue"),
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
        ([7, 7.5], -44, "blue"),
        ([8, 8.5], -44, "red"),
        ([9, 9.5], -44, "green"),
    ]
    return [create_threshold_line(x, y, color) for x, y, color in legend_configs]


def create_critical_handover_line(sliders):
    return [
        go.Scatter(
            x=[-8, 5],
            y=[sliders["a2criticalthresholdrsrp"]] * 2,
            mode="lines+markers+text",
            line=dict(color="red", shape="spline"),
            text=["", "A2 Critical HO"],
            textposition="bottom center",
            textfont=dict(color="red", size=15),
            marker=dict(
                symbol=["circle", "arrow-bar-up"], size=15, angleref="previous"
            ),
        )
    ]


def create_spline_lines(mappings):
    spline_configs = [
        ("blue", mappings["blue_left"], mappings["blue_right"]),
        ("green", mappings["green_left"], mappings["green_right"]),
        ("red", mappings["red_left"], mappings["red_right"]),
    ]
    return [
        create_spline_line(color, left, right) for color, left, right in spline_configs
    ]


def create_spline_line(color, left, right):
    x_values = get_x_values(color)
    y_values = [left, left, right, right]
    marker_symbols = get_marker_symbols(color)

    return go.Scatter(
        x=x_values,
        y=y_values,
        # line=dict(color=color, shape="spline", dash="dashdot"),
        line=dict(color=color, dash="dashdot"),
        mode="lines+markers",
        marker=dict(
            symbol=marker_symbols,
            size=[15, 0, 0, 15] if color != "red" else [15, 0, 0, 15],
            color=color,
            angleref="previous",
        ),
    )


def get_x_values(color):
    return {
        "blue": [-7, -4, -4, 7],
        "green": [-9, -2, -2, 9],
        "red": [-8, 0, 0, 8],
    }[color]


def get_marker_symbols(color):
    default_symbols = ["arrow-bar-up", "circle", "circle", "arrow-bar-up"]
    return ["y-right"] + default_symbols[1:] if color == "red" else default_symbols


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
            sliders["f1_cov_a5threshold1rsrp"],
            f"COV A5Threshold1: {sliders['f1_cov_a5threshold1rsrp']}",
            "red",
        ),
        (
            sliders["f1_a1a2searchthresholdrsrp"],
            f"A1A2 Threshold: {sliders['f1_a1a2searchthresholdrsrp']}",
            "red",
        ),
        (
            sliders["a2criticalthresholdrsrp"],
            f"A2 Critical: {sliders['a2criticalthresholdrsrp']}",
            "red",
        ),
        (sliders["qrxlevminsib1"], f"QRxLevMin: {sliders['qrxlevminsib1']}", "green"),
        (
            mappings["f1_threshservinglow_map"],
            f"ThreshServingLow: {sliders['f1_threshxlow']}",
            "green",
        ),
        (
            mappings["f1_snonintrasearch_map"],
            f"SNonIntraSearch: {sliders['f1_snonintrasearch']}",
            "green",
        ),
        (
            sliders["f1_iflb_a5threshold1rsrp"],
            f"IFLB A5Threshold1: {sliders['f1_iflb_a5threshold1rsrp']}",
            "blue",
        ),
    ]
    right_annotations = [
        (
            mappings["f1_threshxlow_map"],
            f"(Set on F1) ThreshXLow: {sliders['f1_threshxlow']}",
            "green",
        ),
        (
            sliders["f1_cov_a5threshold2rsrp"],
            f"(Set on F1) COV A5Threshold2: {sliders['f1_cov_a5threshold2rsrp']}",
            "red",
        ),
        (
            sliders["f1_iflb_a5threshold2rsrp"],
            f"(Set on F1) IFLB A5Threshold2: {sliders['f1_iflb_a5threshold2rsrp']}",
            "blue",
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
        text="Mobility Actions and Thresholds for the Sticky Carrier Configuration",
        font=dict(family="Arial", size=30, color="rgb(37,37,37)"),
        showarrow=False,
    )


def add_spline_annotations(fig, mappings):
    annotations = [
        ("blue_right", "blue", "A5 IFLB HO"),
        ("red_right", "red", "A5 COVERAGE HO"),
        ("green_right", "green", "Reselect to lower priority"),
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
        (11, 1, "F2 Cell<br> ", "bottom"),
        (-11, 1, "F1 Cell<br> ", "bottom"),
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
        <h2>✨ Sticky Carrier Configuration</h2>
        <div class="key-takeaways">
            <h3>Key Takeaways:</h3>
            <ul>
                <li>In this configuration, the serving frequency is given a higher priority than the neighboring frequency, regardless of which frequency the UE is currently on.</li>
                <li>It's most useful when two carriers have similar coverage properties, allowing Inter-Frequency Load Balancing (IFLB) to distribute UEs in connected mode and maintaining this distribution in idle mode.</li>
                <li>The configuration divides the signal strength plane into three regions (blue, green, and grey) based on key parameters: `threshServingLow` and `threshXLow`.</li>
                <li>Unlike the Equal Priority Configuration, stickiness in the grey region is guaranteed by the standards, as reselection only occurs when both thresholds are met.</li>
                <li>This configuration is not well-suited for pushing UEs strongly towards a particular frequency or for use between two primary LTE coverage layers. It's best used between capacity layers with similar coverage and performance.</li>
                <li>The configuration allows for fine-tuning of both idle mode behavior and connected mode actions, including coverage-triggered handovers and IFLB.</li>
            </ul>
        </div>
        <div class="conclusion">
            <h3>Conclusion:</h3>
            <p>The Sticky Carrier Configuration offers a balanced approach to managing UE distribution across multiple frequency carriers with similar coverage characteristics. It allows network operators to leverage IFLB for efficient load distribution in connected mode while maintaining this distribution in idle mode, leading to more stable and predictable network behavior. This configuration is particularly effective in scenarios where active pushing of UEs to a specific carrier is not required, but maintaining a balanced load across carriers is desirable. By carefully adjusting parameters such as `threshServingLow`, `threshXLow`, and various IFLB thresholds, operators can optimize network performance and ensure efficient use of available carriers. However, implementing this configuration requires careful consideration of the network's specific characteristics. It's not suitable for all scenarios, particularly those involving primary coverage layers or carriers with significantly different coverage properties. In such cases, other configurations like the Equal Priority or Priority Carrier configurations may be more appropriate. Network operators should assess their specific needs, considering factors such as coverage patterns, capacity requirements, and desired load balancing behavior, to determine if the Sticky Carrier Configuration is the best choice for their network environment.</p>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        1. **Idle Mode Actions:**
            - A UE camped on F1 measures other frequencies when the serving RSRP drops below `sNonIntraSearch`.
            - Reselection to F2 occurs if F1 RSRP falls below `threshServingLow` and F2 RSRP is above `threshXLow`.
            - Above `threshServingLow`, the UE remains on F1 regardless of F2's strength.

        2. **Connected Mode Actions - Coverage Triggered:**
            - Triggered by the feature Mobility Control at Poor Coverage using `EVENT_A5`.
            - Handover to F2 occurs when F1 RSRP falls to `A5Threshold1` and F2 RSRP is above `A5Threshold2`.
            - Blind release-with-redirect can be triggered at `A2Critical` if no suitable target is found.

        3. **Connected Mode Actions - IFLB:**
            - IFLB from F1 to F2 occurs when F1 RSRP is below `A5Threshold1` (set to -44 dBm for IFLB) and F2 RSRP is above `A5Threshold2`.
            - `A5Threshold2` is typically set at or above `threshServingLow` to avoid immediate reselection to F1 in idle mode.

        These mobility actions ensure efficient UE reselection and handover, maintaining connectivity and load balancing between cells.

        <span style="color:red"><strong>Nb:</strong> MCPC must be active.
        """,
        unsafe_allow_html=True,
    )
