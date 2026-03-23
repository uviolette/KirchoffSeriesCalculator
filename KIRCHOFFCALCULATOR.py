import streamlit as st
st.markdown("""
<style>
/* Main background */
.stApp {
    background-color: #a62983;
}

/* Text color */
h1, h2, h3, p, div {
    color: black;
}

/* Buttons */
.stButton>button {
    background-color: #e186c8;
    color: black;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)
st.title("❀⋆.ೃ࿔*:･Kirchhoff Calculator°❀⋆.ೃ࿔*:･°❀⁭ ⁭ ")
st.write("‧₊˚♪ 𝄞₊˚⊹ Solve a very simple series circuit using Kirchhoff’s Voltage Law .⋆♱")

# Inputs
V_total = st.number_input("Total Voltage (V) °❀⋆.ೃ࿔*:･⋅˚₊‧ ୨୧ ‧₊˚ ⋅ ", min_value=0.0)
R1 = st.number_input("Resistance R1 (Ω) °❀⋆.ೃ࿔*:･⋅˚₊‧ ୨୧ ‧₊˚ ⋅ ", min_value=0.0)
R2 = st.number_input("Resistance R2 (Ω) °❀⋆.ೃ࿔*:･⋅˚₊‧ ୨୧ ‧₊˚ ⋅ ", min_value=0.0)
if st.button("✶⋆.˚Calculate˙⋆✮"):
    if R1 + R2 == 0:
        st.error("Total resistance cannot be 0")
    else:
        I = V_total / (R1 + R2)
        V1 = I * R1
        V2 = I * R2

        st.success("Results:")
        st.write(f"Current (I): {I} A")
        st.write(f"Voltage across R1: {V1} V")
        st.write(f"Voltage across R2: {V2} V")
