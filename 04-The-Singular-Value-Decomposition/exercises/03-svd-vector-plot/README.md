# Exercise 4.3

Write a MATLAB program (see Lecture 9) which, given a real 2x2 matrix *A*, plots the
right singular vectors *v1* and *v2* in the unit circle and also the left singular
vectors *u1* and *u2* in the appropriate ellipse, as in Figure 4.1. Apply your
program to the matrix (3.7) and also to the 2x2 matrices of Exercise 4.1.

## Solution

I opted for a Python program instead, which I describe here.

### Set up Python environment

```bash
# Install venv to create isolated environment
sudo apt install python3.10-venv

# Temporary shell variable for virtual environment path
VENV_PATH=./.venv

# Manual Poetry installation: https://python-poetry.org/docs/#installing-manually
# Poetry is used to manage package dependencies.
# Create virtual environment for isolated installation
python3 -m venv $VENV_PATH

# Install pip and setuptools
$VENV_PATH/bin/pip install -U pip setuptools

# Install poetry
$VENV_PATH/bin/pip install poetry

# Verify it works properly
./poetry --help
```

The `poetry` file in this directory is a symbolic link to the `poetry` binary located
at `$VENV/bin/poetry`.

### Initialize Project and Run

Having setup the project, we can use poetry to install dependencies and run the script

```bash
# Install dependencies specified specified by poetry.lock and pyproject.toml
./poetry install

# Run script
./poetry run python main.py

# Optionally provide a name of your choice to save the plot figures
./poetry run python main.py plot-of-singular-vectors.png
```
