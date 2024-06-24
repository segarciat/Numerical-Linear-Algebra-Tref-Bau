from qr_mgs import mgs
import numpy as np

if __name__ == '__main__':
	A = np.array([[0.70000, 0.70711], [0.70001, 0.70711]], dtype=np.float64)
	Q, R = mgs(A)
	print(Q)
