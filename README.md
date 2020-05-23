# IB Margin [![image](https://img.shields.io/github/pipenv/locked/python-version/volemont/ib_margin)](https://github.com/volemont/ib_margin) [![image](https://img.shields.io/github/license/volemont/ib_margin)](https://github.com/volemont/ib_margin/blob/master/LICENSE) [![image](https://github.com/volemont/ib_margin/workflows/Test/badge.svg)](https://github.com/volemont/ib_margin/actions?query=workflow%3ATest) [![image](https://img.shields.io/docker/v/volemont/ib_margin)](https://hub.docker.com/r/volemont/ib_margin/tags)

IB Margin: download margins from the Interactive Brokers
[Futures and FOPs Margin Requirements](https://www.interactivebrokers.com/en/index.php?f=26662)
website.

## Quick Start

Make sure you have Docker installed and set up on your machine before following
these instructions. If you don't already have Docker installed, follow the
[official install instructions](https://docs.docker.com/get-docker) for macOS,
Windows or Linux.

Usage demo:

1. Open a terminal or Windows PowerShell.
1. Run below snippet to create or update an existing margin file.

```sh
# Pull latest docker image
docker pull volemont/ib_margin:latest
# Run docker container, download margin and write to ib_margin.csv
docker run --rm -v ${PWD}:/data volemont/ib_margin:latest /data/ib_margin.csv
```

## Development

The project uses the following features to facilitate the development workflow:

- Import sorting with [isort](https://github.com/timothycrosley/isort).
- Formatting with [black](https://github.com/psf/black).
- Linting with [flake8](http://flake8.pycqa.org/en/latest).
- Static typing with [mypy](http://mypy-lang.org).
- Testing with [pytest](https://docs.pytest.org/en/latest).
- Git hooks that run all the above with [pre-commit](https://pre-commit.com).
- Deployment ready with [Docker](https://docker.com).
- Continuous Integration with [GitHub Actions](https://github.com/features/actions).

### Prerequisites

You need Python 3.7 or later. You can have multiple Python versions installed on
the same system. In Debian derivatives you can install Python 3 like this:

```sh
sudo apt-get install python3 python3-pip
```

For other Linux flavors, macOS and Windows, packages are available at
[Python.org](http://www.python.org/getit).

### Setup

The project uses [Pipenv](https://pipenv.pypa.io) to automatically create and
manage its virtualenv.

```sh
# Install development dependencies
python3 -m pip install -U pipenv
pipenv install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

### Workflow

Modify code and execute the project or run features:

```sh
# Update margins
pipenv run python -m ib_margin ib_margin.csv

# Sort imports, format, lint, static type and test the project
pipenv run pre-commit run --all-files
```

## Credits

This package was created with
[Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the
[sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter)
project template.
