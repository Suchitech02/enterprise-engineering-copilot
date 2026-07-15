import json

import streamlit as st

from copilot.generator.project_generator import ProjectGenerator
from copilot.models.bronze import (
    BronzeGenerationRequest,
    BronzeGenerationResponse,
)
from copilot.ui.client import CopilotClient

client = CopilotClient()

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

    try:

        parsed_json = json.loads(sample_response)

        response = client.generate_bronze(
            api_name=api_name,
            endpoint=endpoint,
            authentication=authentication,
            description=description,
            sample_response=parsed_json,
        )

        bronze_response = BronzeGenerationResponse(**response)

        request = BronzeGenerationRequest(
            api_name=api_name,
            endpoint=endpoint,
            authentication=authentication,
            description=description,
            sample_response=parsed_json,
        )

        files = ProjectGenerator.generate_files(
            request,
            bronze_response,
        )

        st.success("Bronze pipeline generated successfully!")

        st.header("Summary")
        st.write(bronze_response.summary)

        st.divider()

        st.header("Python Code")
        st.code(bronze_response.python_code, language="python")

        st.divider()

        st.header("SQL Code")
        st.code(bronze_response.sql_code, language="sql")

        st.divider()

        st.header("Folder Structure")
        st.code(bronze_response.folder_structure)

        st.divider()

        st.header("Quality Rules")
        for rule in bronze_response.quality_rules:
            st.write(f"• {rule}")

        st.divider()

        st.header("Assumptions")
        for assumption in bronze_response.assumptions:
            st.write(f"• {assumption}")
        
        st.divider()

        st.subheader("Download Generated Files")

        for filename, content in files.items():
            st.download_button(
                label=f"Download {filename}",
                data=content,
                file_name=filename,
            )

        st.divider()

    except json.JSONDecodeError:
        st.error("Sample Response must be valid JSON.")

    except Exception as ex:
        
        st.error(f"Failed to generate Bronze pipeline: {ex}")