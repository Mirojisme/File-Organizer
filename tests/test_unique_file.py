from organize import unique_file_name
import os


def test_unique_file(tmp_path):
    tmp_file = tmp_path / "test_file.txt"
    tmp_file.write_text("This is a test file.")

    result_path = unique_file_name(str(tmp_path), "test_file.txt")

    assert result_path == str(tmp_path / "test_file_1.txt")