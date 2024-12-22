import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

A = np.array([[5, -1], [7, -1], [9, -1], [7, -3], [11, -1], [-9, 3]])

A7 = np.array([-20, 0])
A8 = np.array([20, 0])
points = np.vstack([A, A7, A8])

vor1 = Voronoi(A)

fig1 = voronoi_plot_2d(vor1)

plt.xlim([-50, 50])
plt.ylim([-50, 50])

vor2 = Voronoi(points)

fig2 = voronoi_plot_2d(vor2)

plt.xlim([-70, 70])
plt.ylim([-70, 70])

plt.show()

