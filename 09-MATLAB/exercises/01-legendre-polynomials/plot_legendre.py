import numpy as np
from numpy import linalg
import matplotlib
import matplotlib.pyplot as plt


def approximate_legendre(k : int = 3, n : int = 7) -> np.array:
	"""
		Uses a Vandermonde of size 2 ** n to approximate the Legendre polynomials
		through degree k on the interval [-1, 1]
	"""
	if k < 0:
		raise ValueError('k must be a nonegative degree')
	if (n <= 0):
		raise ValueError('n must be a positive exponent')

	# Discretize interval [-1, 1]
	x = np.linspace(-1, 1, 2 ** n)

	# Construct Vandermonde matrix
	A = np.column_stack(tuple(x ** i for i in range(k + 1)))

	# Compute reduced QR factorization
	Q, R  = linalg.qr(A, mode='reduced')

	# Scale by last row
	scale_row = 1 / Q[-1, :]
	Q_scaled = Q @ np.diagflat(scale_row)

	# Free memory
	del scale_row, Q
	
	return Q_scaled

if __name__ == '__main__':
	# Compute approximate and exact legendre polynomials on [-1, 1]
	n = 8
	approx_legendre = approximate_legendre(n=n)
	
	# Compute exact Legend Polynomials
	x = np.linspace(-1, 1, 2 ** n)
	exact_legendre = np.column_stack((
		x ** 0,
		x ** 1,
		(3/2) * (x ** 2) - 1/2,
		(5/2) * (x ** 3) - (3/2) * (x ** 1)
	))

	# Plot
	matplotlib.use('qtagg')
	fig, (ax1, ax2) = plt.subplots(1, 2)
	fig.suptitle(f"Approximating Legendre Polynomials with Vandermonde Matrix, $n={n}$")

	# Plot approximations
	ax1.plot(approx_legendre)
	ax1.legend(('$k=0$', '$k=1$', '$k=2$', '$k=3$'))
	ax1.set_title("Discrete Legendre Approximation\nwith QR $[-1, 1]$")

	# Plot error in approximations
	ax2.plot(exact_legendre - approx_legendre)
	ax2.set_title("Error in Discrete Legendre\nApproximation with QR on $[-1, 1]$")
	ax2.legend(('$k=0$', '$k=1$', '$k=2$', '$k=3$'))
	
	plt.show()

