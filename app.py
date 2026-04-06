from pathlib import Path

import streamlit as st

data_path = Path(__file__) / "data" / "processed"
st.set_page_config(layout="wide")

st.write("hello world")
