import streamlit as st
import pandas as pd



st.title("🧹 Fill Null Values")

# Match your original variable name
filee = st.file_uploader("Choose a CSV file", type=["csv"])

if filee is not None:
    file = pd.read_csv(filee)  # Use your variable name `file`
    st.subheader("Original Data")
    st.dataframe(file)
    
    option = st.selectbox(
        "Fill with",
        ("Mean","Minimum","Mode"))

    if(st.button("Generate")):
        if (option =="Mean"):
            file.fillna((file.mean(numeric_only=True)),inplace = True)
        if (option =="Min"):
            file.fillna((file.min(numeric_only=True)),inplace = True)
        if (option =="Mode"):
            file.fillna((file.mode().iloc[0]),inplace = True)
        
    st.dataframe(file)
