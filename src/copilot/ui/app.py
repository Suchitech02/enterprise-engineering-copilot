import json

import streamlit as st

from copilot.generator.project_generator import ProjectGenerator
from copilot.generator.zip_generator import ZipGenerator
from copilot.models.bronze import (
    BronzeGenerationRequest,
    BronzeGenerationResponse,
)
from copilot.services.test_generation_service import UnitTestGenerationService
from copilot.ui.client import CopilotClient

client = CopilotClient()

test_service = UnitTestGenerationService()

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

        generated_test = test_service.generate(
            bronze_response.python_code,
        )

        request = BronzeGenerationRequest(
            api_name=api_name,
            endpoint=endpoint,
            authentication=authentication,
            description=description,
            sample_response=parsed_json,
        )

        files = ProjectGenerator.generate_files(
            request=request,
            response=bronze_response,
            generated_test=generated_test,
        )

        zip_bytes = ZipGenerator.generate_zip(files)

        st.success("Bronze pipeline generated successfully!")

        summary_tab, python_tab, sql_tab, folder_tab, quality_tab, assumptions_tab = st.tabs(
            [
                "Summary",
                "Python",
                "SQL",
                "Folder Structure",
                "Quality Rules",
                "Assumptions",
            ]
        )

        with summary_tab:
            st.header("Summary")
            st.write(bronze_response.summary)

        with python_tab:
            st.header("Python Code")
            st.code(bronze_response.python_code, language="python")

        with sql_tab:
            st.header("SQL Code")
            st.code(bronze_response.sql_code, language="sql")

        with folder_tab:
            st.header("Folder Structure")
            st.code(
                bronze_response.folder_structure,
                language="text",
            )

        with quality_tab:
            st.header("Quality Rules")
            for rule in bronze_response.quality_rules:
                st.write(f"• {rule}")

        with assumptions_tab:
            st.header("Assumptions")
            for assumption in bronze_response.assumptions:
                st.write(f"• {assumption}")

        zip_name = api_name.strip().lower().replace(" ", "_") or "bronze_pipeline"

        st.subheader("Download Generated Files")

        st.download_button(
            label="Download Project (.zip)",
            data=zip_bytes,
            file_name=f"{zip_name}.zip",
            mime="application/zip",
        )

    except json.JSONDecodeError:
        st.error("Sample Response must be valid JSON.")

    except Exception as exc:
        st.error(f"Failed to generate Bronze pipeline: {exc}")
