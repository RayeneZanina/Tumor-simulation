import numpy as np

def initialize_grid_2d(distribution, grid_dims):
    grid_density = np.zeros(grid_dims)
    for i in range(grid_dims[0]):
        for j in range(grid_dims[1]):
            grid_density[i, j] = distribution()
    grid_concentration = np.zeros(grid_dims)
    return grid_density, grid_concentration

def initialize_grid_3d(distribution, grid_dims):
    grid_density = np.zeros(grid_dims)
    for i in range(grid_dims[0]):
        for j in range(grid_dims[1]):
            for k in range(grid_dims[2]):
                grid_density[i, j, k] = distribution()
    grid_concentration = np.zeros(grid_dims)
    return grid_density, grid_concentration
