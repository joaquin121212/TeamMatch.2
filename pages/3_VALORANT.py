import streamlit as st
import webbrowser as wb

st.header("AQUÍ PODRÁS SUBIR TU CURRÍCULUM DE PRO PLAYER PARA SER CONTACTADO POR UN EQUIPO ", divider="violet")
st.write("déjanos aquí tu currículum para que los equipos puedan explorar tu perfil")
# con este codigo funciona nuestro boton


Link1 = '[CURRICULUM](https://docs.google.com/forms/d/e/1FAIpQLSfrhtvK5mlkRqVL_2UgsL0PhrAKRJlLeO5pPZqorLzvK0ycZw/viewform?usp=sf_link)'
st.markdown(Link1, unsafe_allow_html=True)
