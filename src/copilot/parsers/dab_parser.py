from copilot.models.dab import DABGenerationResponse


class DABParser:
    """Parser for Databricks Asset Bundle generation response."""

    @staticmethod
    def clean_code_block(
        content: str,
        language: str,
    ) -> str:
        """Remove markdown code fences."""

        return content.replace(f"```{language}", "").replace("```", "").strip()

    @staticmethod
    def parse_list(
        content: str,
    ) -> list[str]:
        """Convert numbered output into a list."""

        items: list[str] = []

        for line in content.splitlines():
            line = line.strip()

            if not line or line.startswith("```"):
                continue

            if ". " in line:
                _, line = line.split(". ", 1)

            items.append(line)

        return items

    @staticmethod
    def parse(
        answer: str,
    ) -> DABGenerationResponse:
        """Parse an LLM response."""

        sections: dict[str, str] = {}

        current_section: str | None = None
        current_content: list[str] = []

        for line in answer.splitlines():
            if line.startswith("## "):
                if current_section:
                    sections[current_section] = "\n".join(current_content).strip()

                current_section = (
                    line.replace("## ", "").strip().rstrip(":").upper().replace(" ", "_")
                )

                current_content = []

            else:
                current_content.append(line)

        if current_section:
            sections[current_section] = "\n".join(current_content).strip()

        return DABGenerationResponse(
            summary=sections.get("SUMMARY", ""),
            databricks_yml=DABParser.clean_code_block(
                sections.get("DATABRICKS_YML", ""),
                "yaml",
            ),
            jobs_yml=DABParser.clean_code_block(
                sections.get("JOBS_YML", ""),
                "yaml",
            ),
            pipelines_yml=DABParser.clean_code_block(
                sections.get("PIPELINES_YML", ""),
                "yaml",
            ),
            variables_yml=DABParser.clean_code_block(
                sections.get("VARIABLES_YML", ""),
                "yaml",
            ),
            targets_yml=DABParser.clean_code_block(
                sections.get("TARGETS_YML", ""),
                "yaml",
            ),
            folder_structure=sections.get(
                "FOLDER_STRUCTURE",
                "",
            ),
            assumptions=DABParser.parse_list(
                sections.get("ASSUMPTIONS", ""),
            ),
        )
