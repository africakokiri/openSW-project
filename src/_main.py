import streamlit as st
from _functions import write_sidebar


# 사이드바에 추가할 페이지
pages = [
    {"title": "세대별 인기 관광지 분석", "file_name": "popular_place_per_gen.py"},
]

write_sidebar(pages)
