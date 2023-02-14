# Example setup for python packaging
This repo demonstrates a reasonable starting point for building a python package that has a command line interface.

Setup:
- Command line interface: `click`
- Testing: `pytest`
- Package configuration using `pyproject.toml`
- Backend for building a wheel: `setuptools`
- Code formatting using `black` and `isort`
- Separation of requirements for running and for development

## Example use
```bash
git clone <this repo>
cd ExamplePythonPackage

# create a virtual env
# Using conda here, but use whatever you want
conda create -n foo python=3.10 -y
conda activate foo

# Make editable install the package with the dev dependencies
pip install -e .[dev]

# Run all the tests
pytest

# Try the command line option
# View the help fist, then run it
hello --help
hello Neil -l Dencklau

# Make sure code is formatted consistently
black .
isort --profile black .

# Build a wheel and place it in 'build' directory
# Can take the file build\ExamplePythonPackage* and install on other systems
pip wheel -w build .
```

## Additional recommendations
- Setup `black` and `isort` to run on save (almost all editors support this)
