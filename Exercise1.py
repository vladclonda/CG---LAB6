import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, Delaunay, voronoi_plot_2d, delaunay_plot_2d

points = np.array([[3, -5], [-6, 6], [6, -4], [5, -5], [9, 10]])

vor = Voronoi(points)

delaunay = Delaunay(points)

fig = voronoi_plot_2d(vor)

fig2 = delaunay_plot_2d(delaunay)


plt.show()


