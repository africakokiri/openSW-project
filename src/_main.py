import streamlit as st


# 사이드바에 추가할 페이지
pages = [
    {"title": "세대별 인기 관광지 분석", "file_name": "popular_place_per_gen.py"},
]

# pages 배열에 추가한 사이드바 객체 렌더링
st.navigation(
    [st.Page("introduction.py", title="프로젝트 소개")]
    + [st.Page(page["file_name"], title=page["title"]) for page in pages]
).run()
