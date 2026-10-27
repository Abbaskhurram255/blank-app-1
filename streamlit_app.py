import pandas as pd
import numpy as np
import streamlit as st
from sklearn.datasets import fetch_califormia_housing

st.title("My new app")
st.write(
    "💕All good"
)
penguins: pd.DataFrame = fetch_california_housing(as_frame=True).frame
st.line_plot(penguins, x="flipper_length_mm", y="sex")