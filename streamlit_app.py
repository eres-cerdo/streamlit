import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

options = ["France", "United Kingdom"]
selected_option = st.selectbox("Select a country", options)

st.write("You selected:", selected_option)

if selected_option:
    # Perform query.
    # Uses st.cache_data to only rerun when the query changes or after 10 min.
    @st.cache_data(ttl=600)
    def run_query(query):
        query_job = client.query(query)
        rows_raw = query_job.result()
        # Convert to list of dicts. Required for st.cache_data to hash the return value.
        rows = [dict(row) for row in rows_raw]
        return rows

    rows = run_query(f"SELECT SUM(Quantity * UnitPrice) as GMV FROM `my-data-warehouse-385605.sample_data.ecommerce` WHERE country = '{selected_option}'")

    # Print results.
    st.write(rows)
