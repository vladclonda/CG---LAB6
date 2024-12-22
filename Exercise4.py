import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d


# Points Ai, Bi, Ci for i=0,...,5
A = np.array([[1 - i, i - 1] for i in range(6)])
B = np.array([[i, -i] for i in range(6)])
C = np.array([[0, i] for i in range(6)])

# Combine all points
points = np.vstack([A, B, C])

# Compute Voronoi diagram
vor = Voronoi(points)

fig = voronoi_plot_2d(vor, show_vertices=False)


half_lines = sum(-1 in ridge for ridge in vor.ridge_vertices)
print(f"Number of half-lines in the Voronoi diagram: {half_lines}")

plt.xlim([-20, 20])
plt.ylim([-20, 20])
plt.show()

