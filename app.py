from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="PD, PI e PID pelo LGR", layout="wide")

html = (Path(__file__).parent / "apptotal.html").read_text(encoding="utf-8")
components.html(html, height=1800, scrolling=True)
