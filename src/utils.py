# coding=utf-8
import streamlit as st


def set_slider():
    DEFAULT_WIDTH = 60
    width = st.slider(
        label="", min_value=0, max_value=100, value=DEFAULT_WIDTH, format="%d%%"
    )

    width = max(width, 0.01)
    side = max((100 - width) / 2, 0.01)
    _, container, _ = st.columns([side, width, side])
    return container

