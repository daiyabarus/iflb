import plotly.graph_objs as go
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_vertical_slider import vertical_slider as svs
from styles import multi_color_styling


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
<<<<<<< HEAD:layout/test_priority.py
=======
            "a2 Critical",
>>>>>>> 50dbd91067fb2acf4b32efbf38f30220da8e5766:test.py
            1,
            -140,
            -44,
            -123,
            "#AAE89F",
            "lightgrey",
            "#5DC93E",
<<<<<<< HEAD:layout/test_priority.py
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
=======
>>>>>>> 50dbd91067fb2acf4b32efbf38f30220da8e5766:test.py
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
        "f1_threshxhigh": create_slider(
            columns[3],
            "threshxhigh",
            2,
            0,
            62,
            22,
            "#008000",
            "lightgray",
            "#F1C40F",
        ),
        "f1_iflb_a5threshold1rsrp": create_slider(
            columns[4],
            "iflba5threshold1rsrp",
<<<<<<< HEAD:layout/test_priority.py
=======
            "LB a5Threshold1Rsrp",
>>>>>>> 50dbd91067fb2acf4b32efbf38f30220da8e5766:test.py
            1,
            -140,
            -44,
            -50,
<<<<<<< HEAD:layout/test_priority.py
            "#0000FF",
=======
            "#28BBDD",
>>>>>>> 50dbd91067fb2acf4b32efbf38f30220da8e5766:test.py
            "lightgray",
            "#F1C40F",
        ),
        "f1_iflb_a5threshold2rsrp": create_slider(
            columns[5],
            "iflba5threshold2rsrp",
<<<<<<< HEAD:layout/test_priority.py
=======
            "LB a5Threshold2Rsrp",
>>>>>>> 50dbd91067fb2acf4b32efbf38f30220da8e5766:test.py
            1,
            -140,
            -44,
            -96,
            "#0000FF",
            "lightgray",
            "#F1C40F",
        ),
        "f2_threshservinglow": create_slider(
            columns[6],
            "f2threshservinglow",
            2,
            0,
            62,
            4,
            "#008000",
            "lightgray",
            "#C1392B",
        ),
        "f2_threshxlow": create_slider(
            columns[7],
            "f2_threshXLow",
            2,
            0,
            62,
            4,
            "#008000",
            "lightgray",
            "#C1392B",
        ),
        "f2_snonintrasearch": create_slider(
            columns[8],
            "f2_snonintrasearch",
            2,
            0,
            62,
            6,
            "#008000",
            "lightgray",
            "#C1392B",
        ),
        "f2_a1a2searchthresholdrsrp": create_slider(
            columns[9],
            "f2_a1a2searchthresholdrsrp",
<<<<<<< HEAD:layout/test_priority.py
=======
            "a1a2 ThresholdRsrp",
>>>>>>> 50dbd91067fb2acf4b32efbf38f30220da8e5766:test.py
            1,
            -140,
            -44,
            -110,
            "#FA0101",
            "lightgray",
            "#C1392B",
        ),
        "f2_cov_a5threshold1rsrp": create_slider(
            columns[10],
            "f2_cov_a5threshold1rsrp",
<<<<<<< HEAD:layout/test_priority.py
=======
            "A5 a5Threshold1Rsrp",
>>>>>>> 50dbd91067fb2acf4b32efbf38f30220da8e5766:test.py
            1,
            -140,
            -44,
            -100,
            "#FA0101",
            "lightgray",
            "#C1392B",
        ),
        "f2_cov_a5threshold2rsrp": create_slider(
            columns[11],
            "f2_cov_a5threshold2rsrp",
<<<<<<< HEAD:layout/test_priority.py
=======
            "A5 a5Threshold2Rsrp",
>>>>>>> 50dbd91067fb2acf4b32efbf38f30220da8e5766:test.py
            1,
            -140,
            -44,
            -106,
            "#FA0101",
            "lightgray",
            "#C1392B",
        ),
        "f2_iflb_a5threshold1rsrp": create_slider(
            columns[12],
            "f2iflba5threshold1rsrp",
<<<<<<< HEAD:layout/test_priority.py
=======
            "LB a5Threshold1Rsrp",
>>>>>>> 50dbd91067fb2acf4b32efbf38f30220da8e5766:test.py
            1,
            -140,
            -44,
            -80,
            "#0000FF",
            "lightgray",
            "#C1392B",
        ),
        "f2_iflb_a5threshold2rsrp": create_slider(
            columns[13],
            "f2iflba5threshold2rsrp",
<<<<<<< HEAD:layout/test_priority.py
=======
            "LB a5Threshold2Rsrp",
>>>>>>> 50dbd91067fb2acf4b32efbf38f30220da8e5766:test.py
            1,
            -140,
            -44,
            -90,
<<<<<<< HEAD:layout/test_priority.py
            "#0000FF",
=======
            "#9CA3DB",
>>>>>>> 50dbd91067fb2acf4b32efbf38f30220da8e5766:test.py
            "lightgray",
            "#C1392B",
        ),
    }
    return slider_values


def generate_scripts(sliders):
    script_lines = [
        "# SET ON F1",
        f'set EUtranCell.DD=[F1],UeMeasControl=.,ReportConfigSearch= a2criticalthresholdrsrp$ {sliders["a2criticalthresholdrsrp"]}',
        f'set EUtranCell.DD=[F1] qRxLevMin$ {sliders["qrxlevminsib1"]}',
        f'set EUtranCell.DD=[F1],EUtranFreqRelation=[F2] qRxLevMin$ {sliders["qrxlevmin"]}',
        f'set EUtranCell.DD=[F1],EUtranFreqRelation=[F2] threshXHigh$ {sliders["f1_threshxhigh"]}',
        f'set EUtranCell.DD=[F1],UeMeasControl=.,ReportConfigEUtraInterFreqLb= a5Threshold1Rsrp$ {sliders["f1_iflb_a5threshold1rsrp"]}',
        f'set EUtranCell.DD=[F1],UeMeasControl=.,ReportConfigEUtraInterFreqLb= a5Threshold2Rsrp$ {sliders["f1_iflb_a5threshold2rsrp"]}',
        "# SET ON F2",
        f'set EUtranCell.DD=[F2],UeMeasControl=.,ReportConfigSearch= a2criticalthresholdrsrp$ {sliders["a2criticalthresholdrsrp"]}',
        f'set EUtranCell.DD=[F2] qRxLevMin {sliders["qrxlevminsib1"]}',
        f'set EUtranCell.DD=[F2] threshServingLow$ {sliders["f2_threshservinglow"]}',
        f'set EUtranCell.DD=[F2],EUtranFreqRelation=[F1] threshXLow$ {sliders["f2_threshxlow"]}',
        f'set EUtranCell.DD=[F2] systemInformationBlock3 sNonIntraSearch={sliders["f2_snonintrasearch"]}',
        f'set EUtranCell.DD=[F2],UeMeasControl=.,ReportConfigSearch= a1a2SearchThresholdRsrp$ {sliders["f2_a1a2searchthresholdrsrp"]}',
        f'set EUtranCell.DD=[F2],UeMeasControl=.,ReportConfigA5= a5Threshold1Rsrp$ {sliders["f2_cov_a5threshold1rsrp"]}',
        f'set EUtranCell.DD=[F2],UeMeasControl=.,ReportConfigA5= a5Threshold2Rsrp$ {sliders["f2_cov_a5threshold2rsrp"]}',
        f'set EUtranCell.DD=[F2],UeMeasControl=.,ReportConfigEUtraInterFreqLb= a5Threshold1Rsrp$ {sliders["f2_iflb_a5threshold1rsrp"]}',
        f'set EUtranCell.DD=[F2],UeMeasControl=.,ReportConfigEUtraInterFreqLb= a5Threshold2Rsrp$ {sliders["f2_iflb_a5threshold2rsrp"]}',
    ]

    script = "\n".join(script_lines)
    return script


def compute_threshold_mappings(sliders):
    f1_threshxhigh_map = (sliders["f1_threshxhigh"] * 2) + sliders["qrxlevmin"]
    f2_threshservinglow_map = (sliders["f2_threshservinglow"] * 2) + sliders[
        "qrxlevmin"
    ]
    f2_threshxlow_map = (sliders["f2_threshxlow"] * 2) + sliders["qrxlevmin"]
    f2_snonintrasearch_map = (sliders["f2_snonintrasearch"] * 2) + sliders[
        "qrxlevminsib1"
    ]
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
            line=dict(color="red", dash="dot"),
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
                ((sliders["qrxlevmin"] + max_value) / 1.5),
                ((sliders["qrxlevmin"] + max_value) / 1.5),
                ((f1_threshxhigh_map + max_value) / 2),
                ((f1_threshxhigh_map + max_value) / 2),
            ],
            line=dict(color="green", shape="spline", dash="dashdot"),
<<<<<<< HEAD:layout/test_priority.py
            marker=dict(symbol="arrow-bar-up", size=15, angleref="previous"),
=======
            marker=dict(symbol="arrow-bar-up", size=20, angleref="previous"),
>>>>>>> 50dbd91067fb2acf4b32efbf38f30220da8e5766:test.py
        ),
        go.Scatter(
            x=[-12, -6, 6, 16],
            y=[
                (
                    (
                        sliders["a2criticalthresholdrsrp"]
                        + sliders["f1_iflb_a5threshold1rsrp"]
                    )
                    / 1.5
                ),
                (
                    (
                        sliders["a2criticalthresholdrsrp"]
                        + sliders["f1_iflb_a5threshold1rsrp"]
                    )
                    / 1.5
                ),
                (sliders["f1_iflb_a5threshold2rsrp"] - max_value / 2),
                (sliders["f1_iflb_a5threshold2rsrp"] - max_value / 2),
            ],
            line=dict(color="blue", shape="spline", dash="dashdot"),
<<<<<<< HEAD:layout/test_priority.py
            marker=dict(symbol="arrow-bar-up", size=15, angleref="previous"),
=======
            marker=dict(symbol="arrow-bar-up", size=20, angleref="previous"),
>>>>>>> 50dbd91067fb2acf4b32efbf38f30220da8e5766:test.py
        ),
        go.Scatter(
            x=[16, 10, -2, -14],
            y=[
                (
                    (
                        sliders["a2criticalthresholdrsrp"]
                        + sliders["f2_cov_a5threshold1rsrp"]
                    )
                    / 2
                ),
                (
                    (
                        sliders["a2criticalthresholdrsrp"]
                        + sliders["f2_cov_a5threshold1rsrp"]
                    )
                    / 2
                ),
                ((sliders["f2_cov_a5threshold2rsrp"] + max_value) / 2),
                ((sliders["f2_cov_a5threshold2rsrp"] + max_value) / 2),
            ],
            line=dict(color="red", shape="spline", dash="dashdot"),
<<<<<<< HEAD:layout/test_priority.py
            marker=dict(symbol="arrow-bar-up", size=15, angleref="previous"),
=======
            marker=dict(symbol="arrow-bar-up", size=20, angleref="previous"),
>>>>>>> 50dbd91067fb2acf4b32efbf38f30220da8e5766:test.py
        ),
        go.Scatter(
            x=[19, 10, -2, -16],
            y=[
                ((f2_threshservinglow_map + sliders["qrxlevmin"]) / 2),
                ((f2_threshservinglow_map + sliders["qrxlevmin"]) / 2),
                ((f2_threshxlow_map + max_value) / 2.5),
                ((f2_threshxlow_map + max_value) / 2.5),
            ],
            line=dict(color="green", shape="spline", dash="dashdot"),
<<<<<<< HEAD:layout/test_priority.py
            marker=dict(symbol="arrow-bar-up", size=15, angleref="previous"),
=======
            marker=dict(symbol="arrow-bar-up", size=20, angleref="previous"),
>>>>>>> 50dbd91067fb2acf4b32efbf38f30220da8e5766:test.py
        ),
        go.Scatter(
            x=[18, 10, -2, -10],
            y=[
                (
                    (
                        sliders["a2criticalthresholdrsrp"]
                        + sliders["f2_cov_a5threshold1rsrp"]
                    )
                    / 2.2
                ),
                (
                    (
                        sliders["a2criticalthresholdrsrp"]
                        + sliders["f2_cov_a5threshold1rsrp"]
                    )
                    / 2.2
                ),
                ((sliders["f2_iflb_a5threshold2rsrp"] + max_value) / 2.5),
                ((sliders["f2_iflb_a5threshold2rsrp"] + max_value) / 2.5),
            ],
            line=dict(color="blue", shape="spline", dash="dashdot"),
<<<<<<< HEAD:layout/test_priority.py
            marker=dict(symbol="arrow-bar-up", size=15, angleref="previous"),
=======
            marker=dict(symbol="arrow-bar-up", size=20, angleref="previous"),
>>>>>>> 50dbd91067fb2acf4b32efbf38f30220da8e5766:test.py
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
        "F1 a2CriticalThresholdRsrp",
        "F1 qRxLevMin",
        "(set on F2)<br>threshXLow",
        "(set on F2)<br>ReportConfigA5 a5Threshold2Rsrp",
        "(set on F2)<br>ReportConfigEUtraInterFreqLb a5Threshold2Rsrp",
        "ReportConfigEUtraInterFreqLb a5Threshold1Rsrp",
    ]

    colors_left = ["blue", "blue", "green", "red", "blue", "blue"]

    labels_right = [
        "F2 a2CriticalThresholdRsrp",
        "F2 qRxLevMin",
        "ReportConfigA5 a5Threshold1Rsrp",
        "a1a2SearchThresholdRsrp",
        "threshServingLow",
        "sNonIntraSearch",
        "(set on F1)<br>ReportConfigEUtraInterFreqLb a5Threshold2Rsrp",
        "ReportConfigEUtraInterFreqLb a5Threshold1Rsrp",
        "(set on F1) threshXHigh",
    ]
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

    max_len_left = len(y_data_left)
    max_len_right = len(y_data_right)
    max_len = max(max_len_left, max_len_right)

    for i in range(max_len):
        if i < max_len_left:
            y_trace = y_data_left[i]
            label = labels_left[i]
            color = colors_left[i]
            annotations.append(
                dict(
                    x=-22,
                    y=y_trace,
                    xanchor="right",
                    yanchor="middle",
                    text=f"{label}:{y_trace}",
                    font=dict(family="Ericsson Hilda Light", size=12, color=color),
                    showarrow=False,
                    xref="x",
                    yref="y",
                )
            )
        if i < max_len_right:
            y_trace = y_data_right[i]
            label = labels_right[i]
            color = colors_right[i]
            annotations.append(
                dict(
                    x=22,
                    y=y_trace,
                    xanchor="left",
                    yanchor="middle",
                    text=f"{label}:{y_trace}",
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
            x=-0.25,
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


def styling(text, font_size=10, text_align="center"):
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
        "F1 & F2<br>a2criticalthresholdrsrp<br>&emsp;&emsp;&emsp;",
        "F1 & F2<br>qRxLevMin<br>SIB1",
        "F1 & F2<br>qRxLevMin<br>SIB3",
        "F1<br>threshXHigh<br>&emsp;&emsp;&emsp;",
        "F1<br>ReportConfigEUtraInterFreqLb<br>a5Threshold1Rsrp",
        "F1<br>ReportConfigEUtraInterFreqLb<br>a5Threshold2Rsrp",
        "F2<br>threshServingLow<br>&emsp;&emsp;&emsp;",
        "F2<br>threshXLow<br>&emsp;&emsp;&emsp;",
        "F2<br>sNonIntraSearch<br>&emsp;&emsp;&emsp;",
        "F2<br>a1a2searchthresholdrsrp<br>&emsp;&emsp;&emsp;",
        "F2<br>ReportConfigA5<br>a5Threshold1Rsrp",
        "F2<br>ReportConfigA5<br>a5Threshold2Rsrp",
        "F2<br>ReportConfigEUtraInterFreqLb<br>a5Threshold1Rsrp",
        "F2<br>ReportConfigEUtraInterFreqLb<br>a5Threshold2Rsrp",
    ]

    for column, text in zip(columns, column_texts):
        with column.container():
            st.markdown(styling(text), unsafe_allow_html=True)

    container = st.container()
    with container:
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
                st.code(generated_script, language="bash")

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
