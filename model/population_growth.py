import numpy as np 

def drug_source(concentration, position, grid_dims):
    source = np.zeros(grid_dims)
    source[position] = concentration
    return source

def update_concentration(concentration_grid, source, diffusion_rate, dt = 0.01, dx = 0.1):
    laplacian = (np.roll(concentration_grid, 1, axis=0) +
                 np.roll(concentration_grid, -1, axis=0) +
                 np.roll(concentration_grid, 1, axis=1) +
                 np.roll(concentration_grid, -1, axis=1) -
                 4 * concentration_grid) / dx**2
    return concentration_grid + (diffusion_rate * laplacian + source) * dt

def update_concentration_3d(concentration_grid, source, diffusion_rate, dt = 0.01, dx = 0.1):
    laplacian = (np.roll(concentration_grid, 1, axis=0) + np.roll(concentration_grid, -1, axis=0) +
                 np.roll(concentration_grid, 1, axis=1) + np.roll(concentration_grid, -1, axis=1) +
                 np.roll(concentration_grid, 1, axis=2) + np.roll(concentration_grid, -1, axis=2) -
                 6 * concentration_grid) / dx**2
    return concentration_grid + (diffusion_rate * laplacian + source) * dt

def drug_effect(concentration_grid, EC50 = 0.5, hill_coefficient = 1):
    return concentration_grid**hill_coefficient / (EC50**hill_coefficient + concentration_grid**hill_coefficient)

def update_density(density_grid, drug_effect_grid, growth_rate = 0.05, alpha = 0.1, dt = 0.01):
    return density_grid + (growth_rate * density_grid * (1 - density_grid) - alpha * drug_effect_grid * density_grid) * dt

