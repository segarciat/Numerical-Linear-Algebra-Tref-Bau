import numpy as np
from numpy import linalg

def mgs(A: np.array) -> (np.array, np.array):
	""" 
		Given matrix m by n matrix A with m >= n, computes the QR factorization
		and returns matrices Q and R. Q is unitary, and R is upper-triangular.

		Uses the modified Gram Schmidt Orthogonalization procedure.

		Based on Algorithm 8.1 in Numerical Linear Algebra by Trefethen and Bau
	"""

	m, n = A.shape
	if m < n:
		raise ValueError("Column count exceeds row count")
	
	Q = np.zeros((m, n))
	R = np.zeros((n, n))

	V = A.copy()

	for i in range(n):
		# Compute diagonal entry and normalize q_i
		v_i = V[:, i]
		r_ii = linalg.norm(v_i)
		q_i = v_i / r_ii

		R[i, i] = r_ii
		Q[:, i] = v_i / r_ii
		for j in range(i + 1, n):
			# Remove component in direction of q_i
			v_j = V[:, j]
			r_ij = np.dot(q_i, v_j)
			V[:, j] = v_j - r_ij * q_i
	return (Q, R)
