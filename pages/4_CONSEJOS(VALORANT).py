import streamlit as st
import webbrowser as wb

# con el webbrowser podemos configurar y personalizar nuestros botones
st.header("AQUÍ ENCONTRARÁS VIDEOS PARA MEJORAR  ", divider="violet")

link2 = '[RUTINA DE AIM]("https://www.youtube.com/watch?v=DeFSBVQmjYg")'
st.markdown(link2, unsafe_allow_html=True)
st.header("", divider="violet")   

link3 = '[POSICIONAMIENTO]("https://www.youtube.com/watch?v=T1nrBfH5ghA")'
st.markdown(link3, unsafe_allow_html=True)
st.header("", divider="violet")

link4 = '[MIRA]("https://www.youtube.com/watch?v=SfIq646Xy98")'
st.markdown(link4, unsafe_allow_html=True)        