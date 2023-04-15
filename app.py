import streamlit as st
from recommend_page import show_recommendations
from Top20_page import show_top_20

st.markdown('<link rel="stylesheet" href="styles.css">', unsafe_allow_html=True)

page = st.sidebar.selectbox("Select", ("Recommend", "Top 20 Books"))

if page == "Recommend":
    show_recommendations()
else:
    show_top_20()