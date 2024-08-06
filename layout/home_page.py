import streamlit as st

# sys = platform.system()
# work_dir = (
#     os.path.dirname(os.path.abspath(__file__))
#     .replace("src\\layout", "")
#     .replace("src/layout", "")
# )


def homepage():
    # set_page_width(900)
    st.markdown(
        """
    # 📡 Mobility Configurations📡

    ### ✨ Key Features

    | Mobility Configuration | Priority settings | Idle behavior | Load control | Ideal use case |
    |------------------------|--------------------|--------------------|---------------|-----------------|
    | **Equal Priority** | The two frequencies are given equal priority. | Above a configurable signal strength threshold, UEs remain on the serving frequency. Below the threshold UEs are free to reselect to the other frequency if stronger. | IFLB is configured to work in the zone where UEs remain on the serving frequency. | Ideally suited for use between two "coverage layers" whose cells are not co-sited, as it allows UEs to select the stronger of the two at low signal strengths. Can also be used instead of the "sticky carrier" configuration described below. |
    | **Sticky Carrier** | The serving frequency is given a higher priority than the other frequency. | Above a configurable signal strength threshold UEs remain on the serving frequency. Below the threshold UEs can reselect the other (lower priority) frequency if it is above a second threshold. | IFLB is configured to work in the zone where UEs remain on the serving frequency. | Best used between capacity layers whose coverage is not too different. Allows IFLB to manage load distribution and respects this distribution in idle mode unless the signal strength drops too low. |
    | **Priority Carrier** | One frequency is given a higher priority than the other frequency. | UEs reselect to the higher priority frequency provided its level is above a configurable signal strength threshold. | The idle mode priority push is the primary mechanism for load distribution. | This configuration is best used between frequencies with very different coverage footprints and/or capacities, where it is necessary to actively push UEs to the frequency with the higher capacity and/or poorer coverage. |
    """
    )
    st.markdown(
        """
    <style>
    .left-align {
        text-align: center;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
    ### ✨ Mapping
    """,
        unsafe_allow_html=True,
    )
    st.latex(
        r"""
    \text{ThreshServingLow} = \text{QRxLevMinSIB1} + (\text{qRxLevMinOffset} + (\text{threshServingLow} \times \text{resolution}))
    """
    )

    st.latex(
        r"""
    \text{sNonIntraSearch} = \text{QRxLevMinSIB1}  + (\text{qRxLevMinOffset} + (\text{sNonIntraSearch} \times  \text{resolution}))
    """
    )

    st.latex(
        r"""
    \text{ThreshXHigh} = \text{QRxLevMinSIB3} + (\text{qRxLevMinOffset} + (\text{ThreshXHigh}\times   \text{resolution}))
    """
    )

    st.latex(
        r"""
    \text{ThreshXLow} = \text{QRxLevMinSIB3}  + (\text{qRxLevMinOffset} + (\text{threshXLow} \times \text{resolution}))
    """
    )
