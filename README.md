# Numerical Linear Algebra

This repository contains my notes from and solutions to exercises in the book
[Numerical Linear Algebra](https://epubs.siam.org/doi/pdf/10.1137/1.9781611977165.fm),
by Lloyd N. Trefethen and David Bau, III.

## Experiments and Implementations in Python

The book encourages the use of MATLAB for performing numerical experiments and to
implement the algorithms developed throughout the lectures. I chose to go against
this advice and to use Python instead. The following sections describe the steps
I generally take to set up my environment.

### Creating an isolated environment

To ensure my code is reproducible, I opted to use *Poetry*, a tool used for dependency
management and packaging in Python. See [Poetry docs](https://python-poetry.org/docs/).

```bash
# Ensure it is installed to create virtual environments.
sudo apt install python3.10-venv

# Install pip and setuptools.
# Create virtual environment and install Poetry. See Poetry manual installation: https://python-poetry.org/docs/
mkdir foo-exercise
cd foo-exercise
VENV_PATH=./.venv
python3 -m venv $VENV_PATH
$VENV_PATH/bin/pip install -U pip setuptools
$VENV_PATH/bin/pip install poetry

# Create symlink to the isolated poetry executable installed to $VENV_PATH
ln -s $VENV_PATH/bin/poetry ./poetry

# Verify it works properly
./poetry --help
```

### Initializing Project with Poetry

Having setup the project, we can use poetry to install dependencies:

```bash
# Interactively create pyproject.toml
./poetry init

# Install dependencies specified, creates poetry.lock
./poetry install

# Add and install dependencies after initial configuration
./poetry add numpy
./poetry add matplotlib

```

### Running Script

After creating a script and adding some code, use `poetry run`:

```bash
# Create script and populate with code
vim plot_singular_vectors.py

# Run script
./poetry run python plot_singular_vectors.py
```
