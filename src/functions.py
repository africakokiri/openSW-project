import streamlit as st
import pandas as pd

# csv 파일을 불러와서 출력한다.
def write_csv(csv_path):
  df = pd.DataFrame(pd.read_csv(csv_path, encoding="cp949"))
  
  st.dataframe(df, hide_index=True)