import streamlit as st
import streamlit_antd_components as sac

from layout import homepage, page_config, run_equal, run_priority, run_sticky


def init_session_state():
    if "selected_functionality" not in st.session_state:
        st.session_state["selected_functionality"] = None


def run_app():
    page_config()
    tab_idx = sac.tabs(
        items=[
            sac.TabsItem("Home", icon="house-door-fill"),
            sac.TabsItem("Equal", icon="1-circle-fill"),
            sac.TabsItem("Sticky", icon="2-circle-fill"),
            sac.TabsItem("Priority", icon="3-circle-fill"),
        ],
        align="center",
        return_index=True,
        color="cyan",
        use_container_width=True,
    )

    if tab_idx == 0:
        homepage()
    elif tab_idx == 1:
        run_equal()
    elif tab_idx == 2:
        run_sticky()
    elif tab_idx == 3:
        run_priority()
