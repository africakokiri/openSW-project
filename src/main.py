import streamlit as st
from functions import write_csv

st.markdown("# Hello World!")
write_csv("csv/popular_place_gen_all.csv")
