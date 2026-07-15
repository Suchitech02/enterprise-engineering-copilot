import streamlit as st
import json

st.set_page_config(
    page_title="Enterprise Engineering Copilot",
    layout="wide",
)

st.title("Enterprise Engineering Copilot")

st.subheader("Generate Databricks Bronze Ingestion Pipelines")

with st.form(key="bronze_generation_form"):

    api_name = st.text_input(
        "API Name",
        placeholder="Customer API",
    )

    endpoint = st.text_input(
        "Endpoint",
        placeholder="https://api.company.com/customers",
    )

    authentication = st.selectbox(
        "Authentication",
        [
            "OAuth2",
            "Bearer Token",
            "API Key",
            "Basic Auth",
        ],
    )

    description = st.text_area(
        "Description",
        placeholder="Returns customer master data",
    )

    sample_response = st.text_area(
        "Sample Response (JSON)",
        height=250,
        placeholder='{"customerId": 1001, "customerName": "Alice"}',
    )

    generate = st.form_submit_button("Generate Bronze Pipeline")

if generate:

    st.success("Form submitted successfully!")

    st.write("API Name:", api_name)
    st.write("Endpoint:", endpoint)
    st.write("Authentication:", authentication)
    st.write("Description:", description)

    try:
        parsed_json = json.loads(sample_response)
        st.json(parsed_json)
    except json.JSONDecodeError:
        st.error("Sample Response must be valid JSON.")
