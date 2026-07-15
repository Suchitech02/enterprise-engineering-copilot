import zipfile
from io import BytesIO

from copilot.generator.zip_generator import ZipGenerator

def test_generate_zip():

    files = {
        "a.txt": "Hello",
        "b.txt": "World",
    }

    zip_bytes = ZipGenerator.generate_zip(files)

    archive = zipfile.ZipFile(BytesIO(zip_bytes))

    assert "a.txt" in archive.namelist()
    assert "b.txt" in archive.namelist()

    assert archive.read("a.txt").decode() == "Hello"