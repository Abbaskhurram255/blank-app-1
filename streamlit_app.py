import pandas as pd
import numpy as np
import streamlit as st

st.title("My new app")
st.write(
    "💕All good"
)
penguins: pd.DataFrame = sns.load_dataset("penguins")
st.line_plot(penguins, x="flipper_length_mm", y="sex")