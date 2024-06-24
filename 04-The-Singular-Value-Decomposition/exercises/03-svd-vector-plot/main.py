from plot_singular_vectors import svd_and_plot
import matplotlib
import numpy as np

if __name__ == '__main__':	
	# See: https://matplotlib.org/stable/users/explain/figure/backends.html#what-is-a-backend
	# Changes from the default non-interactive Agg backend, since that is useful only to write to files
	matplotlib.use('qtagg')
	A = np.array([[1, 2], [0, 2]])
	svd_and_plot(A)
