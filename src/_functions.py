import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim


# csv 파일을 불러와서 화면에 출력한다.
# 첫 번째 인자: csv 파일 경로
# 두 번째 인자: 표시할 column
def write_csv(csv_path, selected_columns):
    df = pd.read_csv(csv_path, encoding="cp949")

    st.dataframe(df[selected_columns], hide_index=True)


# 주소를 기반으로 좌표를 알아낸다.
def geocode_address(address):
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None


# pages 배열에 추가한 사이드바 객체 렌더링
def write_sidebar(pages):
    st.navigation(
        [st.Page("introduction.py", title="프로젝트 소개")]
        + [st.Page(page["file_name"], title=page["title"]) for page in pages]
    ).run()
