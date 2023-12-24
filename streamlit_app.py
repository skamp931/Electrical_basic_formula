import streamlit as st
import math
import time

st.title("**電気工学等の基本公式計算**")

# Using object notation
with st.sidebar:
    add_selectbox = st.selectbox(
    "種類",
    ("電気工学_基本", "電気工学_電磁気", "架線", "地質")
    )

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

if add_selectbox =="電気工学_基本":
    st.write("**電気工学_基本**")
    st.write("園児")

if add_selectbox =="電気工学_電磁気":
    st.write("小学生の時にかかる費用")
    st.write("小学")

if add_selectbox =="架線":
    st.write("高校生の時にかかる費用")
    st.write("高校")

if add_selectbox =="地質":
    st.write("高校生の時にかかる費用")
    st.write("高校")

with st.sidebar:
#    with st.echo():
#        st.write("This code will be printed to the sidebar.")

#    with st.spinner("Loading..."):
#        time.sleep(5)
    st.success("Done!")

st.write("https://hegtel.com/koshiki-denki.html")
    
