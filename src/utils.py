# coding=utf-8
import streamlit as st

class selectValues():
    def __init__(self):
        self.points = ['腕', '肘', '膝', '頭', '投げ手', '足']
        self.timings = ['投げ始め', 'リリース時', '投げ終わり']
        self.evaluates = ['○', '×']
        self.total_evaluates = ['未評価', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


def set_slider():
    DEFAULT_WIDTH = 60
    width = st.slider(
        label="", min_value=0, max_value=100, value=DEFAULT_WIDTH, format="%d%%"
    )

    width = max(width, 0.01)
    side = max((100 - width) / 2, 0.01)
    _, container, _ = st.columns([side, width, side])
    return container


