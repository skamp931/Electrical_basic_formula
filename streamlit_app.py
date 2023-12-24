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
    st.image("./image/orm.jpg")
    col1, col2,col3 = st.columns(3)
 
    with col1:
        st.write('電圧V（ボルト）を求める')
        orm_1 = st.number_input("抵抗R")
        ampea_1 = st.number_input("電流I")
        #volt_1 = st.empty()
        volt_1 = orm_1 * ampea_1
        st.write(f"{volt_1}")
        
    with col2:
        st.write('電流I（アンペア）を求める')
        orm_2 = st.number_input("抵抗R")
        volt_2 = st.number_input("電圧V")
        ampea_2 = st.empty() 
        ampea_2.write(volt_2 * orm_2)

    with col3:
        st.write('抵抗R（オーム）を求める')
        volt_3 = st.number_input("電圧V")
        ampea_3 = st.number_input("電流I")
        orm_3 = st.empty() 
        orm_3.write(volt_3 * ampea_3)


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
    
