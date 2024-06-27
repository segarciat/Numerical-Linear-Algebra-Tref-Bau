from plot_singular_vectors import svd_and_plot
import matplotlib
import numpy as np
import sys
import argparse

if __name__ == '__main__':

	matrices = [
		np.array([[1, 2], [0,  2]]),			# Equation 3.7, Example 3.1
		np.array([[3, 0], [0, -2]]),			# 4.1a
		np.array([[2, 0], [0,  3]]),			# 4.1b
		np.array([[0, 2], [0,  0], [0, 0]]),	# 4.1c
		np.array([[1, 1], [0,  0]]),			# 4.1d
		np.array([[1, 1], [1,  1]]),			# 4.1e
	]
	for A, prefix in zip(matrices, ['eq37', 'a', 'b', 'c', 'd', 'e']):
		figure_save_path = f'{prefix}_{sys.argv[1]}' if len(sys.argv) > 1 else None
		svd_and_plot(A, figure_save_path=figure_save_path)
