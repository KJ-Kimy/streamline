import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="주식증감현황"
)

st.title("주주현황 대시보드")
st.subheader("주식증감내역")


data = pd.read_csv('/df_1110.csv')
# NaN 값을 특정 값으로 채워서 비교
data['종목발행사유명'] = data['종목발행사유명'].fillna('결측치')
st.dataframe(data)

# CSV 파일을 읽어들임
df_1110 = pd.read_csv('df_1110.csv')




# 멀티필터
st.subheader("종목발행사유 필터")
def select(data):
    x = data.종목발행사유명.unique().tolist()
    codes = st.multiselect("종목발행사유명", x, key="key1")

    if codes:
        data = data.query("종목발행사유명 in @codes")

    return data


df = select(data) # <---- add this line
st.write("필터:")
st.dataframe(df)
