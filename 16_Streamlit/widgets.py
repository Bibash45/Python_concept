import streamlit as st
import pandas as pd


st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")

age = st.slider("Select your age:",0,100,25)



if name:
    st.write(f"Hello, {name}!")
if age:
    st.write(f"Your age is {age}")


options=['Python',"Java","C++","Javascript"]
choice = st.selectbox("Choose your favourite language:",options)
st.write(f"you selected {choice}")

data = {
    "Name":["John","Jane","Bibash","Dipesh"],
    "Age":[20,21,22,23],
    "Country":["USA","UK","Nepal","India"]
}
df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)


uploaded_file = st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    u_df = pd.read_csv(uploaded_file)
    st.write(u_df)