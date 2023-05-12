import streamlit as st
from streamlit.components.v1 import html
import webbrowser

def search_on_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    return search_url

def search_on_taobao(query):
    search_url = f"https://www.taobao.com/search?q={query}"
    return search_url

# Streamlit app
def main():
    st.title("Search App")
    query = st.text_input("Enter your search term:")
    if st.button("Search"):
        if query:
            google_url = search_on_google(query)
            taobao_url = search_on_taobao(query)
            html_string = f'''
                <h2 style="font-size: 24px; color: green;">Google Search:</h2>
                <a href="{google_url}" target="_blank" style="font-size: 18px;">Open Google Search Results</a>
                <h2 style="font-size: 24px; color: green;">Taobao Search:</h2>
                <a href="{taobao_url}" target="_blank" style="font-size: 18px;">Open Taobao Search Results</a>
            '''
            html(html_string)
        else:
            st.warning("Please enter a search term.")

if __name__ == "__main__":
    main()
