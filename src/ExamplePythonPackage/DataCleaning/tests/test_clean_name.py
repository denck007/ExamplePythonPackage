import pytest

from ExamplePythonPackage.DataCleaning import clean_name


def test_no_last_name():
    first_name = "a"
    last_name = None

    name = clean_name.name_from_first_and_last(first_name, last_name)
    assert (
        name == f"a"
    ), f"Failed to create correct 'name' from {first_name=} {last_name=}, got {name}"


def test_full_name():
    first_name = "a"
    last_name = "bCDe"

    name = clean_name.name_from_first_and_last(first_name, last_name)
    assert (
        name == f"a bCDe"
    ), f"Failed to create correct 'name' from {first_name=} {last_name=}, got {name}"


def test_full_name():
    first_name = "a"
    last_name = "bCDe"

    name = clean_name.name_from_first_and_last(first_name, last_name)
    assert (
        name == f"a bCDe"
    ), f"Failed to create correct 'name' from {first_name=} {last_name=}, got {name}"


def test_no_first_name():
    first_name = None

    with pytest.raises(
        ValueError, match=r".*on-blank value for `first_name` was not given, got.*"
    ):
        clean_name.name_from_first_and_last(first_name)
