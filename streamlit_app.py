import streamlit as st
import pandas as pd

# Set the title of the web app
st.title("CSV File Uploader")

# Create a file uploader and prompt the user to upload a CSV file
csv_file = st.file_uploader("Upload a CSV file", type=["csv"])

# If the user has uploaded a CSV file
if csv_file is not None:
    # Load the CSV file into a Pandas dataframe
    df = pd.read_csv(csv_file)
    # Display the dataframe in the Streamlit app
    st.write(df)
    
    # Add a button to download the CSV file
    st.download_button(
        label="Download CSV",
        data=df.to_csv().encode("utf-8"),
        file_name="my_csv_file.csv",
        mime="text/csv"
    )
