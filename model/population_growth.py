from turtle import position

import numpy as np 

def laplacian_2d(grid, dx):
    grid_padded = np.pad(grid,1,mode='edge')
    return (grid_padded[2:,1:-1] + grid_padded[:-2,1:-1] +
            grid_padded[1:-1,2:] + grid_padded[1:-1,:-2] -
            4 * grid_padded[1:-1,1:-1]) / dx**2

def laplacian_3d(grid, dx):
    grid_padded = np.pad(grid,1,mode='edge')
    return (grid_padded[2:,1:-1,1:-1] + grid_padded[:-2,1:-1,1:-1] +
            grid_padded[1:-1,2:,1:-1] + grid_padded[1:-1,:-2,1:-1] +
            grid_padded[1:-1,1:-1,2:] + grid_padded[1:-1,1:-1,:-2] -
            6 * grid_padded[1:-1,1:-1,1:-1]) / dx**2

def drug_source(concentration, positions, grid_dims):
    source = np.zeros(grid_dims)
    source[positions[0], positions[1], positions[2]] = concentration
    return source

def update_concentration_perfusion(concentration_grid, density_grid, source, diffusion_rate, dt = 0.01, dx = 0.1, decay = 0.01, beta = 0.05):
    laplacian = laplacian_2d(concentration_grid, dx)
    return concentration_grid + (diffusion_rate * laplacian + source - decay * concentration_grid 
                                 - beta * density_grid * concentration_grid) * dt 

def update_concentration_3d_perfusion(concentration_grid, density_grid, source, diffusion_rate, dt = 0.01, dx = 0.1, decay = 0.01, beta = 0.05):
    laplacian = laplacian_3d(concentration_grid, dx)
    return concentration_grid + (diffusion_rate * laplacian + source - decay * concentration_grid 
                                 - beta * density_grid * concentration_grid) * dt

def update_concentration(concentration_grid,density_grid, diffusion_rate, dt = 0.01, dx = 0.1, decay = 0.01, beta = 0.05):
    laplacian = laplacian_2d(concentration_grid, dx)
    return concentration_grid + (diffusion_rate * laplacian - decay * concentration_grid 
                                 - beta * density_grid * concentration_grid) * dt

def update_concentration_3d(concentration_grid, density_grid, diffusion_rate, dt = 0.01, dx = 0.1, decay = 0.01, beta = 0.05):
    laplacian = laplacian_3d(concentration_grid, dx)
    return concentration_grid + (diffusion_rate * laplacian - decay * concentration_grid 
                                 - beta * density_grid * concentration_grid) * dt

def add_dose(concentration_grid, dose, positions):
    concentration_grid[positions[0], positions[1], positions[2]] += dose
    return concentration_grid

def drug_effect(concentration_grid, EC50 = 0.5, hill_coefficient = 1):
    return concentration_grid**hill_coefficient / (EC50**hill_coefficient + concentration_grid**hill_coefficient)

def update_density(density_grid, drug_effect_grid, growth_rate = 0.05, alpha = 0.1, dt = 0.01, dx = 0.1, movement_rate = 0.01):
    laplacian = laplacian_2d(density_grid, dx)
    return density_grid + (growth_rate * density_grid * (1 - density_grid) - alpha * drug_effect_grid *
                            density_grid + movement_rate * laplacian) * dt

def update_density_3d(density_grid, drug_effect_grid, growth_rate = 0.05, alpha = 0.1, dt = 0.01, dx = 0.1, movement_rate = 0.01):
    laplacian = laplacian_3d(density_grid, dx)
    return density_grid + (growth_rate * density_grid * (1 - density_grid) - (alpha * drug_effect_grid *
                            density_grid) + movement_rate * laplacian) * dt


