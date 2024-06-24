import numpy as np
import math
from numpy import linalg
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches

def angle_from(v: np.array, u: np.array=None) -> float:
	""" Computes angle between v and u. If u is not given, [0, 1] is assumed (angle from x-axis) """
	if u is None:
		u = np.array([0, 1])
	v_norm = linalg.norm(v)
	u_norm = linalg.norm(u)
	return np.arccos(np.clip(np.dot(v / v_norm, u / u_norm), -1, 1)) # Clip to avoid rounding issues.

def plot_right_singular_vectors(Vt: np.array, ax: matplotlib.axes.Axes) -> None:
	""" Plots the right singular vectors from the given V transpose matrix on the given Axes """
	v1, v2 = Vt[0], Vt[1]

	# Plot unit circle
	ax.axis('equal')
	origin = np.array([0, 0])
	unit_circle = matplotlib.patches.Circle(xy=origin, radius=1, fill=False)
	ax.add_patch(unit_circle)

	# Plot right singular vectors
	ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color=['r'], label='$v_1$')
	ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color=['g'], label='$v_2$')

	ax.legend()
	ax.set_title("Right singular vectors")


def plot_left_singular_vectors(U: np.array, s: np.array, ax: matplotlib.axes.Axes) -> None:
	""" 
		Plots the left singular vectors from the given U matrix scaled with the singular values
		on the given Axes
	"""

	# Extract and scale left singular vectors
	sigma1, sigma2 = s
	u1, u2 = U[:, 0], U[:, 1]
	u1_scaled = u1 * sigma1
	u2_scaled = u2 * sigma2
	
	# Plot ellipse
	origin = np.array([0, 0])
	rotation_angle = angle_from(u2_scaled) * (180 / math.pi) # in degrees
	ax.axis('equal')
	ellipse = matplotlib.patches.Ellipse(
		xy=origin, width=2*sigma1, height=2*sigma2, angle=rotation_angle, fill=False
	)
	ax.add_patch(ellipse)

	# Plot left singular vectors
	ax.quiver(0, 0, u1_scaled[0], u1_scaled[1], angles='xy', scale_units='xy',
			scale=1, color=['r'], label='$\sigma_1 \cdot u_1$')
	ax.quiver(0, 0, u2_scaled[0], u2_scaled[1], angles='xy', scale_units='xy',
			scale=1, color=['g'], label='$\sigma_2 \cdot u_2$')
	ax.legend()
	ax.set_title("Left singular vectors")


def svd_and_plot(A : np.array, figname=None) -> None:
	"""
		Given matrix A, computes the SVD and plots the left and right singular vectors.
		If figname is given, saves a file with that name. Otherwise displays the figure.
	"""
	U, s, Vt = linalg.svd(A)
	fig, (ax1, ax2) = plt.subplots(1, 2)
	plot_right_singular_vectors(Vt, ax1)
	plot_left_singular_vectors(U, s, ax2)
	fig.suptitle("Image of unit sphere under linear map")
	plt.show()
