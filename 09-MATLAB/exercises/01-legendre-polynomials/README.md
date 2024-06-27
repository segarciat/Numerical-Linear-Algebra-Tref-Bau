# Exercise 9.1

The goal of this exercise is to approximate the Legendre polynomials of degree 0, 1, 2, and 3. We
start with a Vandermonde matrix and sample points on a discretization of the closed interval *[-1, 1]*.
The Vandermonde matrix is *m by 4*, where *m* is the number of grid points we are sampling, and *4* is one
higher than the highest degree polynomial we are approximation. Then we compute its QR factorization,
and plot matrix *Q*, which represents a discrete approximation of the first degree Legendre Polynomials.
For details see the PDF and the `plot_legendre.py` file.

## Installing and Running

To install, run the following commands:

```bash
# Create a virtual environment
python3 -m venv .venv

# Install Poetry
./.venv/bin/pip install -U pip setuptools
./.venv/bin/pip install -U poetry

# Create symbolic link to Poetry executable
ln -s ./.venv/bin/poetry poetry

# Install project dependencies
./poetry install
```

If you encounter difficulties setting Poetry, see the [Poetry documentation](https://python-poetry.org/docs/#installing-manually).

To run the experiment, execute the following:

```bash
./poetry run python plot_legendre.py
```
