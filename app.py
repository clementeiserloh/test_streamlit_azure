import streamlit as st

st.title("Hello World")

st.markdown("""
<style>
.big-font {
    color: black !important;
    font-size:50px !important;
    display : flex;
    text-align:center
}
</style>
""", unsafe_allow_html=True)

TITRE = '<strong>HEADMIND IA / CHANNEL </strong>'
st.markdown(f'<h1 class="big-font">{TITRE}</h1>', unsafe_allow_html=True)