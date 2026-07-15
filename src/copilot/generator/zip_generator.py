import io
import zipfile

class ZipGenerator:
    """Generate Zip Archives for project files."""

    @staticmethod
    def generate_zip(
        files: dict[str, str],
        zip_filename: str = "project_files.zip",
    ) -> bytes:
        """Return ZIP archive as bytes."""

        buffer = io.BytesIO()

        with zipfile.ZipFile(
            buffer,
            mode="w",
            compression=zipfile.ZIP_DEFLATED,
        ) as archives:
            
            for filename, content in files.items():
                archives.writestr(
                    filename, 
                    content,
                )
        
        buffer.seek(0)

        return buffer.getvalue()