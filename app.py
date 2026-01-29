import streamlit as st
st.write("Do you like Python?")
answer = st.text_input()
if answer=="yes":
  st.write("Great!")
elif answer=="no":
  st.write("you will like it")
