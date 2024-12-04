import streamlit as st

pages = [
    {
        "title": "프로젝트 소개", # title: 사이드바에 표시할 이름
        "file_name": "introduction.py" # file_name: 해당 파일 이름
    },
    {
        "title": "세대별 인기 관광지 분석",
        "file_name": "popular_place_per_gen.py"
    }
]

st.navigation([st.Page(page["file_name"], title=page["title"]) for page in pages]).run() # pages 배열 안의 값들을 반복문을 사용해서 화면에 출력함