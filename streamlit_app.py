import streamlit as st
import pandas as pd


st.title("🎈 My new Streamlit app!")
st.write(
    "This is the beginning!")
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df