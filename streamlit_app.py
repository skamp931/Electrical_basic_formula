import streamlit as st
import math
import time

st.title("**電気工学等の基本公式計算**")

# Using object notation
"""
with st.sidebar:
    add_selectbox = st.selectbox(
    "種類",
    ("電気工学_基本", "電気工学_電磁気", "架線", "地質")
    )
"""
# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "種類",
        ("電気工学_基本", "電気工学_電磁気", "架線", "地質")
    )

if add_radio =="電気工学_基本":
    st.write("*電気工学_基本*")
    col1, col2,col3 = st.columns(3)
 
    with col1:
        st.write('電圧V（ボルト）を求める')
     
    with col2:
        st.write('電流I（アンペア）を求める')

    with col2:
        st.write('抵抗R（オーム）を求める')


if add_radio =="*電気工学_電磁気*":
    st.write("小学生の時にかかる費用")
    st.write("小学")

if add_radio =="*架線*":
    st.write("高校生の時にかかる費用")
    st.write("高校")

if add_radio =="*地質*":
    st.write("高校生の時にかかる費用")
    st.write("高校")

st.write("参考にさせて頂きました。 https://hegtel.com/koshiki-denki.html")
    
