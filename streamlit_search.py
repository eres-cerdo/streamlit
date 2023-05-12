import streamlit as st
import webbrowser

def search_on_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open_new_tab(search_url)

# Streamlit app
def main():
    st.title("Google Search App")
    query = st.text_input("Enter your search term:")
    if st.button("Search"):
        if query:
            search_on_google(query)
            st.success(f"Searching for '{query}'...")
        else:
            st.warning("Please enter a search term.")

if __name__ == "__main__":
    main()
