import streamlit as st


st.title("my age and city app")

age = st.slider("enter your age", min_value=1, max_value=100, value=18)

city = st.selectbox(
    "select your city",
    ["MUMBAI", "DELHI", "BANGALORE", "PUNE", "CHENNAI"]
)

if st.button("show details"):
    st.success(f"Your age is {age} and your city is {city}")
