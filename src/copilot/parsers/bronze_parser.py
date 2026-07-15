from copilot.models.bronze import BronzeGenerationResponse

class BronzeParser:
    """Parser for Bronze Generation Responses."""

    @staticmethod
    def parse_list(content: str) -> list[str]:
        """Convert numbered LLM output into a list of strings."""

        items = []

        for line in content.splitlines():
            line = line.strip()

            if not line:
                continue

            # Remove leading numbers like "1. "
            if ". " in line:
                _, line = line.split(". ", 1)

            items.append(line)

        return items

    @staticmethod
    def parse(answer:str) -> BronzeGenerationResponse:
        sections = {}

        current_section = None
        current_content = []

        for line in answer.splitlines():
            if line.startswith("## "):
                if current_section:
                    sections[current_section] = "\n".join(current_content).strip()

                current_section = (
                    line.replace("## ", "")
                        .strip()
                        .rstrip(":")
                        .upper()
                        .replace(" ", "_")
                )
                current_content = []
            else:
                current_content.append(line)

        if current_section:

            content = "\n".join(current_content).strip()
            if content.endswith("---"):
                content = content[:-3].strip()
            sections[current_section] = content

        return BronzeGenerationResponse(
            summary=sections.get("SUMMARY", ""),
            python_code=sections.get("PYTHON_CODE", ""),
            sql_code=sections.get("SQL_CODE", ""),
            folder_structure=sections.get("FOLDER_STRUCTURE", ""),
            quality_rules=BronzeParser.parse_list(
                sections.get("QUALITY_RULES", "")
            ),
            assumptions=BronzeParser.parse_list(
                sections.get("ASSUMPTIONS", "")
            ),
        )