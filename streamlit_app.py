import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st

st.title("My new app")
st.write(
    "💕All good"
)
penguins: pd.DataFrame = sns.load_dataset("penguins")
st.write(penguins)