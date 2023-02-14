from typing import Optional

import click

from ExamplePythonPackage.DataCleaning import clean_name


@click.command()
@click.argument(
    "first_name",
    type=str,
)
@click.option("-l", "--last-name", type=str, default=None, help="Users last name")
def main(first_name: str, last_name: Optional[str] = None):
    name = clean_name.name_from_first_and_last(first_name, last_name)
    print(f"Hello {name}")


if __name__ == "__main__":
    main()
