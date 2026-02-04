import streamlit as st 
st.title("simple input app")

name = st.txt_input("Enter your name ")

if st.button("submit"):
 st.write()