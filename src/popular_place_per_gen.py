import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components

from _functions import write_csv

st.markdown("## 세대별 인기 관광지 분석")  # 페이지 제목
components.iframe("https://google.com", height=500)

st.markdown(
    """
    <style>
        .stMain{
            width: 1200px !important;
        }
    </style>
""",
    unsafe_allow_html=True,
)

tab_20, tab_30, tab_40, tab_50, tab_60, tab_all = st.tabs(
    ["20대", "30대", "40대", "50대", "60대", "모든 세대"]
)

with tab_20:
    write_csv(
        "csv/popular_place_per_gen_2.csv",
        ["순위", "관심지점명", "주소도로명", "세대검색건수"],
    )

    df = pd.DataFrame([[37.8835, 127.73831]], columns=["lat", "lon"])
    st.map(df)


with tab_30:
    st.header("A cat")
with tab_40:
    st.header("A cat")
with tab_50:
    st.header("A cat")
with tab_60:
    st.header("A cat")
with tab_all:
    st.header("A cat")