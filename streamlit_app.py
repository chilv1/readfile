import streamlit as st
import pandas as pd

CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSs5tRlFEqLz6J-Ubg8Kh3CkYokxMR-bl9VKWCNNSAV4H6KvNDRyGqDTssxh6dbxUpH0NXJyT8Tq430/pub?gid=393036172&single=true&output=csv"

@st.cache_data
def load_data():
    df = pd.read_csv(CSV_URL)
    df.columns = df.columns.str.strip()
    return df

df = load_data()

st.subheader("📌 Header CSV gốc:")
for col in df.columns:
    st.write(f"- {col}")
