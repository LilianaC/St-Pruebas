import streamlit as st


st.sidebar.title("¿Cuáles números multiplicados dan...y sumados dan...")
st.sidebar.caption("Para practicar la factorización hecho por @LilianaMx")
st.sidebar.caption("Visita nuestro canal para mayor información")

with st.expander("Instrucciones:", expanded=True):
    st.markdown("""
    1. Selecciona el nivel
    2. Busca los números que sumados dan..y multiplicados dan 
    3. Presiona 'enviar' para revisar si los datos son correctos.
    
    --- 
    
    ⚙️ Use the 👈 sidebar to change the settings.
    🎈 Share this app with your friends! 
    """)

st.sidebar.header("Ajustes")

metric = st.sidebar.selectbox("Nivel:", ["Sencillo", "Fácil", "Experto"])
metric2 = st.sidebar.checkbox("Nivel:", ["Sencillo", "Fácil", "Experto"])

with st.form("my_form"):
   st.write("Inside the form")
   my_number = st.slider('Pick a number', 1, 10)
   my_color = st.selectbox('Pick a color', ['red','orange','green','blue','violet'])
   st.form_submit_button('Submit my picks')

# This is outside the form
st.write(my_number)
st.write(my_color)
