from typing import Optional


def name_from_first_and_last(first_name: str, last_name: Optional[str] = None) -> str:
    """
    Combine the fist and last name (if given) into the users full name
    """
    if (first_name is None) or (first_name == ""):
        raise ValueError(
            f"A non-blank value for `first_name` was not given, got `{first_name}`"
        )
    if (last_name is None) or (last_name == ""):
        name = first_name
    else:
        name = f"{first_name} {last_name}"

    return name
