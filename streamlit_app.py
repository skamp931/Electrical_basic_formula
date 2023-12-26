import streamlit as st
import math
import time

st.title("**電気工学等の基本公式計算**")

with st.sidebar:
    add_radio = st.radio(
        "種類",
        ("電気工学_基本", "電気工学_電磁気", "架線", "地質","基礎")
    )

#電気工学基本====================================================================
if add_radio =="電気工学_基本":
    st.header('【電気工学_基本】')

    #オームの法則==================================================================
    st.subheader('オームの法則', divider='blue')
    st.image("./image/orm.jpg")
    col1, col2,col3 = st.columns(3)

    label="test",
    min_value=0.000000,
    step=0.000001,
    max_value=0.0005,
    value=0.0000045,
    format="%f",
    
    with col1:
        st.write('電圧V（ボルト）を求める')
        st.latex(r'''IR = V ''')
        orm_1 = st.number_input(label="抵抗R",min_value=0.000000000,step=1.0,max_value=1000000000.0,value=1.0,format="%f",key="1")
        ampea_1 = st.number_input(label="電流I",min_value=0.000000000,step=1.0,max_value=1000000000.0,value=5.0,format="%f",key="2")
        #volt_1 = st.empty()
        volt_1 = orm_1 * ampea_1
        if volt_1.is_integer():
            st.metric(label="電圧V",value=f"{volt_1:,}V")
        else:
            st.metric(label="電圧V",value=f"{volt_1:,.3f}V")

    with col2:
        st.write('電流I（アンペア）を求める')
        st.latex(r'''\frac{V}{R} = I ''')
        orm_1 = st.number_input(label="抵抗R",min_value=0.000000000,step=1.0,max_value=1000000000.0,value=1.0,format="%f",key="3")
        volt_1 = st.number_input(label="電圧V",min_value=0.000000000,step=1.0,max_value=1000000000.0,value=10.0,format="%f",key="4")
        ampea_1 = volt_1 / orm_1 
        if ampea_1.is_integer():
            st.metric(label="電流I",value=f"{ampea_1:,}A")
        else:
            st.metric(label="電流I",value=f"{ampea_1:,.3f}A")
            
    with col3:
        st.write('抵抗R（オーム）を求める')
        st.latex(r'''\frac{V}{I} = R''')
        volt_1 = st.number_input(label="電圧V",min_value=0.000000000,step=1.0,max_value=1000000000.0,value=10.0,format="%f",key="5")
        ampea_1 = st.number_input(label="電流I",min_value=0.000000000,step=1.0,max_value=1000000000.0,value=5.0,format="%f",key="6")
        orm_1 = volt_1 / ampea_1 
        if orm_1.is_integer():
            st.metric(label="抵抗R",value=f"{orm_1:,}Ω")
        else:
            st.metric(label="抵抗R",value=f"{orm_1:,.3f}Ω")
    
    st.write("")
    #抵抗並列接続==================================================================

    st.subheader('抵抗の並列接続', divider='blue')
    st.latex(r''' \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \cdots = R''')
    #st.image("./image/orm.jpg")
    pala = st.number_input("並列数",2)
    orm_pala = []
    if pala > 1:
        for i in range(pala):
            orm_pala.append("")
            orm_pala[i] = st.number_input(label=f"{i+1:d}つ目の抵抗値",min_value=0.000000000,step=1.0,max_value=1000000000.0,value=5.0,format="%f")
    orm_pala_value = sum([1/i for i in orm_pala])
    
    st.metric(label="抵抗R",value=f"{1/orm_pala_value:,.3f}Ω")

    st.write("")
    #抵抗率==================================================================
    st.subheader('抵抗率', divider='blue')
    col4, col5,col6 = st.columns(3)
 
    with col4:
        st.write('抵抗 R を求める')
        st.latex(r''' R = \rho \frac{L}{S} ''')
        rho = st.number_input(label="抵抗率ρ[Ω・ｍ]",min_value=0.000000000,step=1.0,max_value=1000000000.0,value=0.00000010,format="%f",key="10")
        L = st.number_input(label="長さL[m]",min_value=0.000000000,step=1.0,max_value=1000000000.0,value=5.0,format="%f",key="11")
        S = st.number_input(label="断面積S[m2]",min_value=0.000000000,step=1.0,max_value=1000000000.0,value=10.0,format="%f",key="12")
        R_rho_1 = (rho) * L / S
        if R_rho_1.is_integer():
            st.metric(label="抵抗R",value=f"{R_rho_1:,}Ω")
        else:
            st.metric(label="抵抗R",value=f"{R_rho_1:,.3f}Ω")
    
    with col5:
        st.write('抵抗率 ρ を求める')
        st.latex(r''' \rho =  R\frac{S}{L} ''')
        R_rho_2 = st.number_input(label="_抵抗R[Ω]",min_value=0.000000000,step=1.0,max_value=1000000000.0,value=5.0,format="%f",key="13")
        L_2 = st.number_input(label="長さL[m]",min_value=0.000000000,step=1.0,max_value=1000000000.0,value=5.0,format="%f",key="14")
        S_2 = st.number_input(label="断面積S[m2]",min_value=0.000000000,step=1.0,max_value=1000000000.0,value=5.0,format="%f",key="15")
        rho_2 = R_rho_2 * S_2 / L_2
        if rho_2.is_integer():
            st.metric(label="抵抗率ρ",value=f"{rho_2:,}[Ω・ｍ]")
        else:
            st.metric(label="抵抗率ρ",value=f"{rho_2:,.9f}[Ω・ｍ]")

    with col6:
        st.write('導電率 σ を求める')
        st.latex(r''' \sigma = \frac{1}{\rho} ''')
        rho_3 = st.number_input(label="抵抗率ρ[Ω・ｍ]",min_value=0.000000000,step=1.0,max_value=1000000000.0,value=0.000001,format="%f",key="16") 
        sigma_3 = 1 / (rho_3)
        if sigma_3.is_integer():
            st.metric(label="導電率σ",value=f"{sigma_3:,}[S/m]")
        else:
            st.metric(label="導電率σ",value=f"{sigma_3:,.3f}[S/m]")

    #電流の定義==================================================================
    st.write("")
    st.subheader('電荷から電流を求める', divider='blue')
    st.latex(r'''I = \frac{Q}{t}''')
    q_1 = st.number_input(label="電荷Q[C]",min_value=0.000000000,step=1.0,max_value=1000000000.0,value=1.0,format="%f",key="17")
    time_1 = st.number_input(label="時間t[秒]",min_value=0.000000000,step=1.0,max_value=1000000000.0,value=5.0,format="%f",key="18")
    #volt_1 = st.empty()
    ampea_10 = q_1 / time_1
    if ampea_10.is_integer():
        st.metric(label="電流I",value=f"{ampea_10:,}A")
    else:
        st.metric(label="電流I",value=f"{ampea_10:,.3f}A")

    #分圧==================================================================
    st.write("")
    st.subheader('分圧の公式', divider='blue')
    st.latex(r'''V_1 = \frac{R_1}{R_1 + R_2} E''')
    Rbun_1 = st.number_input(label="抵抗R1[Ω]",min_value=0.000000000,step=1.0,max_value=1000000000.0,value=1.0,format="%f",key="19")
    Rbun_2 = st.number_input(label="抵抗R2[Ω]",min_value=0.000000000,step=1.0,max_value=1000000000.0,value=5.0,format="%f",key="20")
    denatu = st.number_input(label="電圧E[V]",min_value=0.000000000,step=1.0,max_value=1000000000.0,value=5.0,format="%f",key="21")
    #volt_1 = st.empty()
    V_bun = (Rbun_1 / (Rbun_1 + Rbun_2)) * denatu
    if V_bun.is_integer():
        st.metric(label="R1にかかる電圧V",value=f"{V_bun:,}V")
    else:
        st.metric(label="R1にかかる電圧V",value=f"{V_bun:,.3f}A")


#電気工学基本====================================================================
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
        radius_k_1 = st.number_input(label="半径r",min_value=0.000000000,step=1.0,max_value=1000000000.0,value=0.5,format="%f",key="17")
        s_k_1 = radius_k_1**2 * math.pi

        if s_k_1.is_integer():
            st.metric(label="面断面積S[m2]",value=f"{S_k_1:,}m2")
        else:
            st.metric(label="面断面積S[m2]",value=f"{S_k_1:,.3f}m2")
    
    with col2_k:
        st.write(' ')

    with col3_k:
        st.write(' ')


for i in range(20):
    st.write("")

st.write("参考にさせて頂きました。 https://hegtel.com/koshiki-denki.html")
    
