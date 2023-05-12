import streamlit as st
from streamlit.components.v1 import html
import webbrowser

def search_on_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    return search_url

def search_on_taobao(query):
    search_url = f"https://s.taobao.com/search?catId=100&from=sea_1_searchbutton&page=1&q={query}&spm=a2141.241046-cn.searchbar.d_2_searchbox&tmhkh5=&type=p"
    return search_url

def search_on_baidu(query):
    search_url = f"https://www.baidu.com/s?wd={query}"
    return search_url

# Open all search result links
def open_all_links():
    query = st.session_state.search_query
    if query:
        google_url = search_on_google(query)
        taobao_url = search_on_taobao(query)
        baidu_url = search_on_baidu(query)
        webbrowser.open_new_tab(google_url)
        webbrowser.open_new_tab(taobao_url)
        webbrowser.open_new_tab(baidu_url)

# Streamlit app
def main():
    st.title("Search App")
    query = st.text_input("Enter your search term:", key="search_query")
    if st.button("Search"):
        if query:
            google_url = search_on_google(query)
            taobao_url = search_on_taobao(query)
            baidu_url = search_on_baidu(query)
            html_string = f'''
                st.button("Open All Links", on_click=open_all_links)
                <h2 style="font-size: 24px; color: green;">Google Search:</h2>
                <a href="{google_url}" target="_blank" style="font-size: 18px;">Open Google Search Results</a>
                <h2 style="font-size: 24px; color: green;">Taobao Search:</h2>
                <a href="{taobao_url}" target="_blank" style="font-size: 18px;">Open Taobao Search Results</a>
                <h2 style="font-size: 24px; color: green;">Baidu Search:</h2>
                <a href="{baidu_url}" target="_blank" style="font-size: 18px;">Open Baidu Search Results</a>
            '''
            html(html_string, height=2000)
            

if __name__ == "__main__":
    main()
