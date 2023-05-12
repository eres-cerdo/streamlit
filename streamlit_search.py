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

def search_on_amazon(query):
    search_url = f"https://www.amazon.com/s?k={query}"
    return search_url

def search_on_ebay(query):
    search_url = f"https://www.ebay.com/sch/i.html?_nkw={query}"
    return search_url

# Open all search result links
def open_all_links():
    query = st.session_state.search_query
    if query:
        google_url = search_on_google(query)
        taobao_url = search_on_taobao(query)
        baidu_url = search_on_baidu(query)
        amazon_url = search_on_amazon(query)
        ebay_url = search_on_ebay(query)
        webbrowser.open(google_url, new=2)
        webbrowser.open(taobao_url, new=2)
        webbrowser.open(baidu_url, new=2)
        webbrowser.open(amazon_url, new=2)
        webbrowser.open(ebay_url, new=2)

# Streamlit app
def main():
    st.title("Search App")
    query = st.text_input("Enter your search term:", key="search_query")
    if st.button("Search"):
        if query:
            google_url = search_on_google(query)
            taobao_url = search_on_taobao(query)
            baidu_url = search_on_baidu(query)
            amazon_url = search_on_amazon(query)
            ebay_url = search_on_ebay(query)
            html_string = f'''
                <h2 style="font-size: 24px; color: green;">Google Search:</h2>
                <a href="{google_url}" target="_blank" style="font-size: 18px;">Open Google Search Results</a>
                <h2 style="font-size: 24px; color: green;">Taobao Search:</h2>
                <a href="{taobao_url}" target="_blank" style="font-size: 18px;">Open Taobao Search Results</a>
                <h2 style="font-size: 24px; color: green;">Baidu Search:</h2>
                <a href="{baidu_url}" target="_blank" style="font-size: 18px;">Open Baidu Search Results</a>
                <h2 style="font-size: 24px; color: green;">Amazon Search:</h2>
                <a href="{amazon_url}" target="_blank" style="font-size: 18px;">Open Amazon Search Results</a>
                <h2 style="font-size: 24px; color: green;">eBay Search:</h2>
                <a href="{ebay_url}" target="_blank" style="font-size: 18px;">Open eBay Search Results</a>
            '''
            html(html_string, height=600)
            st.write(f"Google Search URL: {google_url}")
            st.write(f"Taobao Search URL: {taobao
