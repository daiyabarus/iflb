import streamlit as st
import streamlit_antd_components as sac


def init_session_state():
    if "selected_functionality" not in st.session_state:
        st.session_state["selected_functionality"] = None


sac.tabs(
    [
        sac.TabsItem(label="apple", tag="10"),
        sac.TabsItem(icon="google"),
        sac.TabsItem(label="github", icon="github"),
        sac.TabsItem(label="disabled", disabled=True),
    ],
    align="center",
)
