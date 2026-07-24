from copilot.models.silver import SilverGenerationResponse


class SilverParser:
    """Parser for Silver Generation Responses."""

    @staticmethod
    def clean_code_block(content: str, language: str) -> str:
        return content.replace(f"```{language}", "").replace("```", "").strip()

    @staticmethod
    def parse_list(content: str) -> list[str]:
        """Convert numbered LLM output into a list of strings."""

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
    def parse(answer: str) -> SilverGenerationResponse:
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
            content = "\n".join(current_content).strip()

            if content.endswith("---"):
                content = content[:-3].strip()

            sections[current_section] = content

        python_code = SilverParser.clean_code_block(
            sections.get("PYTHON_CODE", ""),
            "python",
        )

        sql_code = SilverParser.clean_code_block(
            sections.get("SQL_CODE", ""),
            "sql",
        )

        return SilverGenerationResponse(
            summary=sections.get("SUMMARY", ""),
            python_code=python_code,
            sql_code=sql_code,
            transformations=SilverParser.parse_list(sections.get("TRANSFORMATIONS", "")),
            quality_rules=SilverParser.parse_list(sections.get("QUALITY_RULES", "")),
            assumptions=SilverParser.parse_list(sections.get("ASSUMPTIONS", "")),
        )
