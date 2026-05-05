import numpy as np
from model.grid_init import initialize_grid_2d, initialize_grid_3d
from model.parameters import get_default_parameters
from model.population_growth import drug_source, update_concentration, update_concentration_3d, update_density, drug_effect
from visualization.plots import plot_heatmap_midsection
from visualization.animation import animate_heatmap_section

params = get_default_parameters()
time_steps = 3000 # 30 hours

density_grid, concentration_grid = initialize_grid_3d(lambda : np.random.rand(), params.grid_dims)
drug_source_grid = drug_source(params.source_concentration, params.source_position, params.grid_dims)
concentration_grid += drug_source_grid * params.dt
density_grid_history = [density_grid.copy()]
concentration_grid_history = [concentration_grid.copy()]

for t in range(time_steps):
    concentration_grid = update_concentration_3d(concentration_grid, drug_source_grid, params.diffusion_rate, params.dt, params.dx)
    drug_effect_grid = drug_effect(concentration_grid, params.EC50, params.hill_coefficient)
    density_grid = update_density(density_grid, drug_effect_grid, params.r, params.alpha, params.dt)
    density_grid_history.append(density_grid.copy())
    concentration_grid_history.append(concentration_grid.copy())

animate_heatmap_section(density_grid_history, concentration_grid_history, time_steps)
