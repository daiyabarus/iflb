import plotly.graph_objs as go
import streamlit as st
from streamlit_vertical_slider import vertical_slider as svs


def run_priority():
    st.title("Mobility Actions and Thresholds for the Priority Carrier Configuration")

    (
        col1,
        # _,
        col2,
        col3,
        col4,
        col5,
        # _,
        col6,
        col7,
        col8,
        col9,
        col10,
        col11,
    ) = st.columns(11)

    with col1:
        a2criticalthresholdrsrp = svs(
            key="a2criticalthresholdrsrp",
            label="a2CriticalThresholdRsrp",
            step=2,
            min_value=-140,
            max_value=-44,
            default_value=-123,
            slider_color="#2067CE",
            track_color="lightgray",
            thumb_color="#5C59D3",
            height=100,
            value_always_visible=True,
        )
    with col2:
        f1_qrxlevmin = svs(
            key="qrxlevmin",
            label="qRxLevMin SIB3",
            step=2,
            min_value=-140,
            max_value=-44,
            default_value=-120,
            slider_color="#28BBDD",
            track_color="lightgray",
            thumb_color="#EA5D32",
            height=100,
            value_always_visible=True,
        )
    with col3:
        f1_threshxhigh = svs(
            key="threshxhigh",
            label="threshXHigh",
            step=2,
            min_value=0,
            max_value=62,
            default_value=16,
            slider_color="#28BBDD",
            track_color="lightgray",
            thumb_color="#EA5D32",
            height=100,
            value_always_visible=True,
        )
    with col4:
        f1_iflb_a5threshold1rsrp = svs(
            key="iflba5threshold1rsrp",
            label="ReportConfigEUtraInterFreqLb a5Threshold1Rsrp",
            step=2,
            min_value=-140,
            max_value=-44,
            default_value=-100,
            slider_color="#28BBDD",
            track_color="lightgray",
            thumb_color="#EA5D32",
            height=100,
            value_always_visible=True,
        )
    with col5:
        f1_iflb_a5threshold2rsrp = svs(
            key="iflba5threshold2rsrp",
            label="ReportConfigEUtraInterFreqLb a5Threshold2Rsrp",
            step=2,
            min_value=-140,
            max_value=-44,
            default_value=-110,
            slider_color="#28BBDD",
            track_color="lightgray",
            thumb_color="#EA5D32",
            height=100,
            value_always_visible=True,
        )

    with col6:
        f2_qrxlevmin = svs(
            key="f2qrxlevmin",
            label="qRxLevMin SIB3",
            step=2,
            min_value=-140,
            max_value=-44,
            default_value=-120,
            slider_color="#9CA3DB",
            track_color="lightgray",
            thumb_color="#E0CA3C",
            height=100,
            value_always_visible=True,
        )
    with col7:
        f2_threshxlow = svs(
            key="f2threshxlow",
            label="threshXLow",
            step=2,
            min_value=0,
            max_value=62,
            default_value=6,
            slider_color="#9CA3DB",
            track_color="lightgray",
            thumb_color="#E0CA3C",
            height=100,
            value_always_visible=True,
        )
    with col8:
        f2_threshservinglow = svs(
            key="f2threshservinglow",
            label="threshServingLow",
            step=2,
            min_value=0,
            max_value=62,
            default_value=2,
            slider_color="#9CA3DB",
            track_color="lightgray",
            thumb_color="#E0CA3C",
            height=100,
            value_always_visible=True,
        )
    with col9:
        f2_cov_a5threshold1rsrp = svs(
            key="f2cova5threshold1rsrp",
            label="ReportConfigA5 a5Threshold1Rsrp",
            step=2,
            min_value=-140,
            max_value=-44,
            default_value=-108,
            slider_color="#9CA3DB",
            track_color="lightgray",
            thumb_color="#E0CA3C",
            height=100,
            value_always_visible=True,
        )
    with col10:
        f2_cov_a5threshold2rsrp = svs(
            key="f2cova5threshold2rsrp",
            label="ReportConfigA5 a5Threshold2Rsrp",
            step=2,
            min_value=-140,
            max_value=-44,
            default_value=-110,
            slider_color="#9CA3DB",
            track_color="lightgray",
            thumb_color="#E0CA3C",
            height=100,
            value_always_visible=True,
        )
    with col11:
        f2_iflb_a5threshold1rsrp = svs(
            key="f2iflba5threshold1rsrp",
            label="ReportConfigEUtraInterFreqLb a5Threshold1Rsrp",
            step=2,
            min_value=-140,
            max_value=-44,
            default_value=-90,
            slider_color="#9CA3DB",
            track_color="lightgray",
            thumb_color="#E0CA3C",
            height=100,
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

    f2_threshxlow_map = (f2_threshxlow * 2) + f2_qrxlevmin
    f1_threshxhigh_map = (f1_threshxhigh * 2) + f1_qrxlevmin
    f2_threshservinglow_map = (f2_threshservinglow * 2) + f2_qrxlevmin
    max_value = -44

    vertical_lines = [
        # TODO: F1 BAR
        # qrxlevmin f1
        create_vertical_line(-45, -140, f1_qrxlevmin),
        create_vertical_line(-45, f1_qrxlevmin, -44, "green"),
        # f2_threshxlow
        create_vertical_line(-40, -140, f2_threshxlow_map),
        create_vertical_line(-40, f2_threshxlow_map, -44, "green"),
        # f2_cov_a5threshold1rsrp
        create_vertical_line(-35, -140, f2_cov_a5threshold2rsrp),
        create_vertical_line(-35, f2_cov_a5threshold2rsrp, -44, "red"),
        # a2criticalthresholdrsrp
        create_vertical_line(-30, -140, a2criticalthresholdrsrp),
        create_vertical_line(
            -30, a2criticalthresholdrsrp, f1_iflb_a5threshold1rsrp, "blue"
        ),
        create_vertical_line(-30, f1_iflb_a5threshold1rsrp, -44),
        # f2_iflb_a5threshold2rsrp
        create_vertical_line(-25, -140, f1_iflb_a5threshold1rsrp),
        create_vertical_line(-25, f1_iflb_a5threshold1rsrp, -44, "blue"),
        # TODO: F2 BAR
        # MARK 1
        create_vertical_line(45, -140, a2criticalthresholdrsrp),
        create_vertical_line(
            45, a2criticalthresholdrsrp, f2_iflb_a5threshold1rsrp, "blue"
        ),
        create_vertical_line(45, f2_iflb_a5threshold1rsrp, -44),
        # MARK 1
        create_vertical_line(45, -140, f1_threshxhigh_map),
        create_vertical_line(45, f1_threshxhigh_map, -44, "green"),
        # MARK 2
        create_vertical_line(40, -140, f2_threshservinglow_map),
        create_vertical_line(40, f2_threshservinglow_map, f2_qrxlevmin, "green"),
        create_vertical_line(40, f2_qrxlevmin, -44),
        # MARK: 3
        create_vertical_line(35, -140, a2criticalthresholdrsrp),
        create_vertical_line(
            35, a2criticalthresholdrsrp, f2_cov_a5threshold1rsrp, "red"
        ),
        create_vertical_line(35, f2_cov_a5threshold1rsrp, -44),
        # MARK: 4
        create_vertical_line(30, -140, f1_iflb_a5threshold2rsrp),
        create_vertical_line(30, f1_iflb_a5threshold2rsrp, -44, "blue"),
    ]

    lines = [
        go.Scatter(
            x=[-50, -45],
            y=[f1_qrxlevmin, f1_qrxlevmin],
            mode="lines+markers",
            line=dict(color="green"),
        ),
        go.Scatter(
            x=[-50, -45],
            y=[max_value, max_value],
            mode="lines+markers",
            line=dict(color="green"),
        ),
        go.Scatter(
            x=[-50, -40],
            y=[f2_threshxlow_map, f2_threshxlow_map],
            mode="lines+markers",
            line=dict(color="green"),
        ),
        go.Scatter(
            x=[-50, -40],
            y=[max_value, max_value],
            mode="lines+markers",
            line=dict(color="green"),
        ),
        go.Scatter(
            x=[-50, -35],
            y=[f2_cov_a5threshold2rsrp, f2_cov_a5threshold2rsrp],
            mode="lines+markers",
            line=dict(color="red"),
        ),
        go.Scatter(
            x=[-50, -35],
            y=[max_value, max_value],
            mode="lines+markers",
            line=dict(color="red"),
        ),
        go.Scatter(
            x=[-50, -30],
            y=[a2criticalthresholdrsrp, a2criticalthresholdrsrp],
            mode="lines+markers",
            line=dict(color="blue"),
        ),
        go.Scatter(
            x=[-50, -30],
            y=[f1_iflb_a5threshold1rsrp, f1_iflb_a5threshold1rsrp],
            mode="lines+markers",
            line=dict(color="blue"),
        ),
        go.Scatter(
            x=[-45, 45],
            y=[a2criticalthresholdrsrp, a2criticalthresholdrsrp],
            mode="lines+markers",
            line=dict(color="blue"),
        ),
        go.Scatter(
            x=[45, 50],
            y=[a2criticalthresholdrsrp, a2criticalthresholdrsrp],
            mode="lines+markers",
            line=dict(color="blue"),
        ),
        go.Scatter(
            x=[45, 50],
            y=[f2_iflb_a5threshold1rsrp, f2_iflb_a5threshold1rsrp],
            mode="lines+markers",
            line=dict(color="blue"),
        ),
        go.Scatter(
            x=[45, 50],
            y=[f1_threshxhigh_map, f1_threshxhigh_map],
            mode="lines+markers",
            line=dict(color="green"),
        ),
        go.Scatter(
            x=[45, 50],
            y=[max_value, max_value],
            mode="lines+markers",
            line=dict(color="green"),
        ),
        go.Scatter(
            x=[40, 50],
            y=[f2_qrxlevmin, f2_qrxlevmin],
            mode="lines+markers",
            line=dict(color="green"),
        ),
        go.Scatter(
            x=[40, 50],
            y=[f2_threshservinglow_map, f2_threshservinglow_map],
            mode="lines+markers",
            line=dict(color="green"),
        ),
        go.Scatter(
            x=[35, 50],
            y=[f2_cov_a5threshold1rsrp, f2_cov_a5threshold1rsrp],
            mode="lines+markers",
            line=dict(color="red"),
        ),
        go.Scatter(
            x=[35, 50],
            y=[a2criticalthresholdrsrp, a2criticalthresholdrsrp],
            mode="lines+markers",
            line=dict(color="red"),
        ),
        go.Scatter(
            x=[30, 50],
            y=[f1_iflb_a5threshold2rsrp, f1_iflb_a5threshold2rsrp],
            mode="lines+markers",
            line=dict(color="blue"),
        ),
        go.Scatter(
            x=[30, 50],
            y=[max_value, max_value],
            mode="lines+markers",
            line=dict(color="blue"),
        ),
        # MARK: Polyline 1
        go.Scatter(
            x=[-45, 45],
            y=[(max_value + f1_qrxlevmin) / 4, (max_value + f1_threshxhigh_map) / 2],
            mode="lines+markers",
            line=dict(color="green", shape="spline"),
            marker=dict(symbol="arrow", size=15, angleref="previous"),
        ),
        go.Scatter(
            x=[-30, 45],
            y=[
                (a2criticalthresholdrsrp + f1_iflb_a5threshold1rsrp) / 4,
                (max_value + f1_iflb_a5threshold2rsrp) / 2,
            ],
            mode="lines+markers",
            line=dict(color="blue", shape="spline"),
            marker=dict(symbol="arrow", size=15, angleref="previous"),
        ),
    ]

    fig = go.Figure(data=lines)

    fig.update_layout(
        shapes=vertical_lines,
        xaxis=dict(range=[-55, 55], showticklabels=False, showgrid=False),
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
    st.plotly_chart(fig)


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
