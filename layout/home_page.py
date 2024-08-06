import streamlit as st


def set_page_width(width: int):
    """Set the page width for a Streamlit app with custom CSS.

    Args:
    ----
        width (int): The maximum width in pixels for the content area.
    """
    style = f"""
    <style>
    .main .block-container {{
        max-width: {width}px;
        padding-left: 1rem;
        padding-right: 1rem;
    }}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def homepage():
    set_page_width(1300)
    st.markdown(
        """
    # 📡LTE Mobility Strategies📡
        """
    )
    css = """
    <style>
        .section {
            # border: 2px solid #f0f0f0;
            padding: 20px;
            margin: 20px 0;
            border-radius: 10px;
        }
        .section h2 {
            color: #2c3e50;
        }
        .section h3 {
            color: #2980b9;
        }
        .section p {
            color: #7f8c8d;
        }
        .key-takeaways {
            background-color: #ecf0f1;
            padding: 10px;
            border-radius: 5px;
        }
        .key-takeaways ul {
            margin-left: 20px;
        }
        .conclusion {
            background-color: #dff9fb;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
    """

    st.markdown(css, unsafe_allow_html=True)

    # Equal Priority Configuration
    st.markdown(
        """
    <div class="section">
        <h2>✨Equal Priority Configuration</h2>
        <div class="key-takeaways">
            <h3>Key Takeaways:</h3>
            <ul>
                <li>In idle mode, UEs reselect between carriers based on relative signal strengths, applying hysteresis and offsets.</li>
                <li>The configuration divides the signal strength plane into three regions (blue, green, and grey), determining UE camping behavior.</li>
                <li>The `SNONINTRASEARCH` parameter controls the "stickiness" of UEs to the serving frequency, which can be useful when combined with load balancing.</li>
                <li>This configuration works well for non-co-located cells but may not be ideal for pushing UEs towards a particular frequency in co-located cells.</li>
                <li>Connected mode actions are governed by coverage-triggered events and Inter-Frequency Load Balancing (IFLB).</li>
                <li>The alignment of various thresholds (e.g., `SNONINTRASEARCH`, `A5THRESHOLD1`) is crucial for ensuring that idle mode behavior and IFLB work harmoniously.</li>
            </ul>
        </div>
        <div class="conclusion">
            <h3>Conclusion:</h3>
            <p>The Equal Priority Configuration offers a flexible approach to managing UE distribution across multiple frequency carriers. It is most effective when dealing with non-co-located cells and when the goal is to allow UEs to select the strongest frequency. However, for more specific traffic steering in co-located cell scenarios, other configurations like the Priority Carrier Configuration may be more suitable. Careful parameter tuning is essential to achieve the desired balance between signal strength-based selection and load-based distribution.</p>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Sticky Carrier Configuration
    st.markdown(
        """
    <div class="section">
        <h2>✨Sticky Carrier Configuration</h2>
        <div class="key-takeaways">
            <h3>Key Takeaways:</h3>
            <ul>
                <li>In this configuration, the serving frequency is given a higher priority than the neighboring frequency, regardless of which frequency the UE is currently on.</li>
                <li>It's most useful when two carriers have similar coverage properties, allowing Inter-Frequency Load Balancing (IFLB) to distribute UEs in connected mode and maintaining this distribution in idle mode.</li>
                <li>The configuration divides the signal strength plane into three regions (blue, green, and grey) based on key parameters: `THRESHSERVINGLOW` and `THRESHXLOW`.</li>
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

    # Priority Carrier Configuration
    st.markdown(
        """
    <div class="section">
        <h2>✨Priority Carrier Configuration</h2>
        <div class="key-takeaways">
            <h3>Key Takeaways:</h3>
            <ul>
                <li>This configuration is typically used when carriers have vastly different coverage areas, such as low band vs. high band or macro cells vs. small cells.</li>
                <li>One carrier is assigned a higher idle mode priority via the `cellReselectionPriority` parameter.</li>
                <li>The configuration divides the signal strength plane into three regions (blue, green, and grey) based on key parameters: `THRESHXHIGH`, `THRESHSERVINGLOW`, and `THRESHXLOW`.</li>
                <li>It provides better control over UE distribution compared to Equal Priority or Sticky Carrier Configurations, balancing between actively pushing UEs to the high-priority carrier and leaving room for Inter-Frequency Load Balancing (IFLB).</li>
                <li>The configuration allows for fine-tuning of both idle mode behavior and connected mode actions, including coverage-triggered handovers and IFLB.</li>
                <li>Careful parameter setting is crucial to ensure that idle mode behavior, coverage fallback, and IFLB work harmoniously.</li>
            </ul>
        </div>
        <div class="conclusion">
            <h3>Conclusion:</h3>
            <p>The Priority Carrier Configuration offers a powerful approach to managing UE distribution across multiple frequency carriers with different coverage characteristics. It is particularly effective in scenarios where one carrier needs to be prioritized to maximize its utilization, while still maintaining overall network efficiency and coverage. The configuration allows network operators to strike a balance between actively pushing UEs to a preferred carrier in idle mode and allowing IFLB to distribute traffic in connected mode. By carefully adjusting parameters such as `THRESHXHIGH`, `THRESHSERVINGLOW`, and various IFLB thresholds, operators can optimize network performance, maximize the use of all available carriers, and ensure seamless coverage transitions. However, implementing this configuration requires careful planning and ongoing optimization. Network operators must consider the specific characteristics of their network, including coverage patterns, capacity requirements, and user behavior, to determine the optimal settings for their particular scenario.</p>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
    ## ✨ Key Features

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
    ## ✨ Mapping
    """,
        unsafe_allow_html=True,
    )
    st.latex(
        r"""
    \text{ThreshServingLow} = \text{QRxLevMinSIB3} + (\text{qRxLevMinOffset} + (\text{threshServingLow} \times \text{resolution}))
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
