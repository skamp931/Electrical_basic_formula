import streamlit as st
import math
import time

st.title("**電気工学等の基本公式計算**")

with st.sidebar:
    add_radio = st.radio(
        "種類",
        ("電気工学_基本", "電気工学_電磁気", "架線", "地質")
    )

if add_radio =="電気工学_基本":
    st.header('【電気工学_基本】')
    st.subheader('オームの法則', divider='blue')
    st.image("./image/orm.jpg")
    col1, col2,col3 = st.columns(3)
 
    with col1:
        st.write('電圧V（ボルト）を求める')
        orm_1 = st.number_input("抵抗R",10.0)
        ampea_1 = st.number_input("電流I",5.0)
        #volt_1 = st.empty()
        volt_1 = orm_1 * ampea_1
        st.write(f"　電圧Vは{volt_1:,.3f}Vです")
        
    with col2:
        st.write('電流I（アンペア）を求める')
        orm_1 = st.number_input("抵抗R_",10.0)
        volt_1 = st.number_input("電圧V_",50.0)
        ampea_1 = volt_1 / orm_1 
        st.write(f"　電流Iは{ampea_1:,.3f}Aです")

    with col3:
        st.write('抵抗R（オーム）を求める')
        volt_1 = st.number_input("電圧V__",50.0)
        ampea_1 = st.number_input("電流I__",5.0)
        orm_1 = volt_1 / ampea_1 
        st.write(f"　抵抗Rは{orm_1:,.3f}Ωです")

    st.write("")
    st.subheader('抵抗の並列接続', divider='blue')
    #st.image("./image/orm.jpg")
    pala = st.number_input("並列数",2)
    orm_pala = []
    if pala > 1:
        for i in range(pala):
            orm_pala.append("")
            orm_pala[i] = st.number_input(f"{i+1:d}つ目の抵抗値",10)
    orm_pala_value = sum([1/i for i in orm_pala])
    st.write(f"　抵抗Rは{1/orm_pala_value:,.3f}Ωです")


if add_radio =="電気工学_電磁気":
    st.header('【電気工学_電磁気】')   
    st.write("作成中")

if add_radio =="架線":
    st.header('【架線】')   
    st.write("作成中")

if add_radio =="地質":
    st.header('【地質】')   
    st.write("作成中")

for i in range(20):
    st.write("")

st.write("参考にさせて頂きました。 https://hegtel.com/koshiki-denki.html")
    
