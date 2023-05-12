import streamlit as st
from streamlit.components.v1 import html
import webbrowser

def search_on_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    return search_url

# Streamlit app
def main():
    st.title("Google Search App")
    query = st.text_input("Enter your search term:")
    if st.button("Search"):
        if query:
            search_url = search_on_google(query)
            html_string = f'<a href="{search_url}" target="_blank">Open Search Results</a>'
            html(html_string, scrolling=True)
        else:
            st.warning("Please enter a search term.")

if __name__ == "__main__":
    main()
