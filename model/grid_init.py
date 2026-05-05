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


def initialize_density_blob(grid_dims, blob_centers, standard_deviation):
    density_grid = np.zeros(grid_dims)
    for blob_center in blob_centers:
        for i in range(grid_dims[0]):
            for j in range(grid_dims[1]):
                for k in range(grid_dims[2]):
                    distance_squared = (i - blob_center[0])**2 + (j - blob_center[1])**2 + (k - blob_center[2])**2
                    density_grid[i, j, k] += max(np.exp(-distance_squared / (2 * standard_deviation**2)) + np.random.normal(0, 0.05),0)
                    density_grid[i, j, k] = min(density_grid[i, j, k], 1.0)
    concentration_grid = np.zeros(grid_dims)
    return density_grid, concentration_grid