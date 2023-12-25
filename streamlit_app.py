import streamlit as st
import math
import time

st.title("**電気工学等の基本公式計算**")

with st.sidebar:
    add_radio = st.radio(
        "種類",
        ("電気工学_基本", "電気工学_電磁気", "架線", "地質","基礎")
    )

if add_radio =="電気工学_基本":
    st.header('【電気工学_基本】')
    st.subheader('オームの法則', divider='blue')
    st.image("./image/orm.jpg")
    col1, col2,col3 = st.columns(3)
 
    with col1:
        st.write('電圧V（ボルト）を求める')
        st.latex(r'''IR = V ''')
        orm_1 = st.number_input("抵抗R",10.0)
        ampea_1 = st.number_input("電流I",5.0)
        #volt_1 = st.empty()
        volt_1 = orm_1 * ampea_1
        st.metric(label="電圧V",value=f"{volt_1:,.3f}V")
        
    with col2:
        st.write('電流I（アンペア）を求める')
        st.latex(r'''\frac{V}{R} = I ''')
        orm_1 = st.number_input("抵抗R_",10.0)
        volt_1 = st.number_input("電圧V_",50.0)
        ampea_1 = volt_1 / orm_1 
        st.metric(label="電流I",value=f"{ampea_1:,.3f}A")

    with col3:
        st.write('抵抗R（オーム）を求める')
        st.latex(r'''\frac{V}{I} = R''')
        volt_1 = st.number_input("電圧V__",50.0)
        ampea_1 = st.number_input("電流I__",5.0)
        orm_1 = volt_1 / ampea_1 
        st.metric(label="抵抗R",value=f"{orm_1:,.3f}Ω")

    st.write("")
    st.subheader('抵抗の並列接続', divider='blue')
    st.latex(r''' \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \cdots = R''')
    #st.image("./image/orm.jpg")
    pala = st.number_input("並列数",2)
    orm_pala = []
    if pala > 1:
        for i in range(pala):
            orm_pala.append("")
            orm_pala[i] = st.number_input(f"{i+1:d}つ目の抵抗値",10.000)
    orm_pala_value = sum([1/i for i in orm_pala])
    st.metric(label="抵抗R",value=f"{1/orm_pala_value:,.3f}Ω")

    st.write("")
    st.subheader('抵抗率', divider='blue')
    col4, col5,col6 = st.columns(3)
 
    with col4:
        st.write('抵抗 R を求める')
        st.latex(r''' R = \rho \frac{L}{S} ''')
        rho = st.number_input("抵抗率ρ[Ω・ｍ]✕10^-8",10.0)
        L = st.number_input("長さL",5.0)
        S = st.number_input("断面積S",10.0)
        R_rho_1 = (rho / 10**8) * L / S
        st.metric(label="抵抗R",value=f"{R_rho_1:,.3f}Ω")
        
    with col5:
        st.write('抵抗率 ρ を求める')
        st.latex(r''' \rho =  R\frac{S}{L} ''')
        R_rho_2 = st.number_input("_抵抗R",10.0)
        L_2 = st.number_input("長さL_",5.0)
        S_2 = st.number_input("断面積S_",10.0)
        rho_2 = R_rho_2 * S_2 / L_2
        st.metric(label="抵抗率ρ",value=f"{rho_2:,.3f}[Ω・ｍ]")

    with col6:
        st.write('導電率 σ を求める')
        st.latex(r''' \sigma = \frac{1}{\rho} ''')
        rho_3 = st.number_input("抵抗率ρ[Ω・ｍ]✕10^-8_",10.0) 
        sigma_3 = 1 / (rho_3/10**8)
        st.metric(label="導電率σ",value=f"{sigma_3:,.f}[S/m]")

if add_radio =="電気工学_電磁気":
    st.header('【電気工学_電磁気】')   
    st.write("作成中")

if add_radio =="架線":
    st.header('【架線】')   
    st.write("作成中")

if add_radio =="地質":
    st.header('【地質】')   
    st.write("作成中")

if add_radio =="基礎":
    st.header('【基礎】')   
    st.subheader('断面積を求める', divider='blue')
    col1_k, col2_k,col3_k = st.columns(3)
 
    with col1_k:
        st.write('面の断面積')
        st.latex(r'''S = πr^{2} ''')
        radius_k_1 = st.number_input("半径r",5.0)
        S_k_1 = radius_1^2 * math.pi()
        st.metric(label="面談面積S",value=f"{S_k_1:,.3f}m2")
        
    with col2_k:
        st.write(' ')

    with col3_k:
        st.write(' ')


for i in range(20):
    st.write("")

st.write("参考にさせて頂きました。 https://hegtel.com/koshiki-denki.html")
    
