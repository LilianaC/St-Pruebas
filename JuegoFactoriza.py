import streamlit as st
import numpy as np
import random
import time

f_list = list(np.arange(-5,6,1))
s_list = list(set(np.arange(-10,11,1)) - set(np.array(f_list)))
e_list = list(set(np.arange(-15,16,1))-set(f_list)-set(s_list))


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

   def dificultad():
       nivel = st.multiselect('Multiselect', ['f','s','e'])
       #nivel = input("¿Qué nivel quieres jugar? (f/s/e) ")
       if nivel == 'f':
           x = random.choice(f_list)
           y = random.choice(f_list)
           nums = [x,y]
           st.markdown("Los números pueden ser: ",f_list) 
           #print("Los números pueden ser: ",f_list)
       
       elif nivel == 's':
           x = random.choice(s_list)
           y = random.choice(s_list)
           nums = [x,y]
           print("Los números pueden ser: ",s_list)

       elif nivel == 'e':
           x = random.choice(e_list)
           y = random.choice(e_list)
           nums = [x,y]
           print("Los números pueden ser: ",e_list)

       m = x*y
       s = x+y
       return nums,m,s


    def revision(xr,yr,nums,start,end):
        if xr in nums and yr in nums :
            print("¡Correcto!")
            elapsed = end-start
            print ("Tiempo de respuesta: ",elapsed)
            print ("¿Quieres jugar otra vez? (s/n)")
            op = input()
            if op == 'n':
                print("¡Gracias por jugar!")
            else:
                op = 's'
        else:
            print("¡Incorrecto!")
            print ("¿Quieres jugar otra vez? (s/n)")
            op = input()
            if op == 'n':
                print("¡Gracias por jugar!")
            else:
                op = 's'
        return op

op = 's'

while op == 's':

  nums, m, s = dificultad()

  print ("¿Cuáles son los números que....?")
  print ("Sumados: ",s)
  print ("Multiplicados: ",m)
  start = time.time()
  xr = int(input("¿Cuál es el primer número? "))
  yr = int(input("¿Cuál es el segundo número? "))
  end = time.time()

  op = revision(xr,yr,nums,start,end)














# This is outside the form
st.write(my_number)
st.write(my_color)
