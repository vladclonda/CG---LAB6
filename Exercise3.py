import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import matplotlib.pyplot as plt

A = np.array([-1, 6])
B = np.array([-1, -1])
C = np.array([4, 7])
D = np.array([6, 7])
E = np.array([1, -1])
F = np.array([-5, 3])
P = np.array([-2, 3])

lambda_vals = np.linspace(0, 100)  

mst_lengths = []

for lambda_val in lambda_vals:

    Q = np.array([2 - lambda_val, 3])
    
    points = np.array([A, B, C, D, E, F, P, Q])
    
    dist_matrix = distance_matrix(points, points)

    mst = minimum_spanning_tree(dist_matrix).toarray()
    
    mst_length = np.sum(mst[mst > 0])

    mst_lengths.append(mst_length)


min_mst_length = min(mst_lengths)
min_lambda = lambda_vals[mst_lengths.index(min_mst_length)]


print(f"The minimum MST length is {min_mst_length:.2f} at lambda = {min_lambda:.2f}")

