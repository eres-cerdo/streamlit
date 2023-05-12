import streamlit as st
import webbrowser

def open_urls(urls):
    for url in urls:
        webbrowser.open_new_tab(url)

# Streamlit app code
st.title("Open Websites")
st.write("Click the button below to open Google.com and Taobao.com.")

# Create a button to open Google.com and Taobao.com
if st.button("Open Google and Taobao"):
    urls = ["https://www.google.com", "https://www.taobao.com"]
    open_urls(urls)
