import os

import pytest

from gendiff import generate_diff


def get_fixture_path(filename):
    return os.path.join("tests", "test_data", filename)


def read_fixture(filename):
    path = get_fixture_path(filename)
    with open(path) as file:
        return file.read()


@pytest.mark.parametrize(
    ("file1", "file2", "expected"),
    [
        ("file1.json", "file2.json", "expected_stylish.txt"),
        ("file1.yml", "file2.yml", "expected_stylish.txt"),
    ],
)
def test_generate_diff_flat_json(file1, file2, expected):
    file_path1 = get_fixture_path(file1)
    file_path2 = get_fixture_path(file2)
    expected_result = read_fixture(expected)

    assert generate_diff(file_path1, file_path2) == expected_result.strip()

