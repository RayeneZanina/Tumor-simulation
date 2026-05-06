import numpy as np
from model.grid_init import *
from model.parameters import get_default_parameters
from model.population_growth import *
from visualization.animation import animate_heatmap_section

params = get_default_parameters()
time_steps = 5000 # 50 hours

def simulate_perfusion(params, time_steps):
    density_grid, concentration_grid = initialize_density_blob(params.grid_dims, params.blob_centers, params.blob_std_dev)
    drug_source_grid = drug_source(params.source_concentration, params.source_positions, params.grid_dims)
    concentration_grid += drug_source_grid * params.dt
    density_grid_history = [density_grid.copy()]
    concentration_grid_history = [concentration_grid.copy()]

    for t in range(time_steps):
        concentration_grid = update_concentration_3d_perfusion(concentration_grid,density_grid, drug_source_grid,
                                                             params.diffusion_rate, params.dt, params.dx, params.decay, params.beta)
        drug_effect_grid = drug_effect(concentration_grid, params.EC50, params.hill_coefficient)
        density_grid = update_density_3d(density_grid, drug_effect_grid, params.r, params.alpha, params.dt, params.dx, params.movement_rate)
        density_grid_history.append(density_grid.copy())
        concentration_grid_history.append(concentration_grid.copy())

    return density_grid_history, concentration_grid_history

def simulate_intervals(params, time_steps):
    density_grid, concentration_grid = initialize_density_blob(params.grid_dims, params.blob_centers, params.blob_std_dev)
    concentration_grid = add_dose(concentration_grid, params.source_concentration, params.source_positions)
    density_grid_history = [density_grid.copy()]
    concentration_grid_history = [concentration_grid.copy()]

    for t in range(time_steps):
        if t % round(params.dose_interval / params.dt) == 0:
            concentration_grid = add_dose(concentration_grid, params.source_concentration, params.source_positions)
        concentration_grid = update_concentration_3d(concentration_grid, density_grid, params.diffusion_rate,
                                                      params.dt, params.dx, params.decay, params.beta)
        drug_effect_grid = drug_effect(concentration_grid, params.EC50, params.hill_coefficient)
        density_grid = update_density_3d(density_grid, drug_effect_grid, params.r, params.alpha, params.dt, params.dx, params.movement_rate)
        density_grid_history.append(density_grid.copy())
        concentration_grid_history.append(concentration_grid.copy())

    return density_grid_history, concentration_grid_history

density_grid_history_perfusion, concentration_grid_history_perfusion = simulate_perfusion(params, time_steps)
density_grid_history_intervals, concentration_grid_history_intervals = simulate_intervals(params, time_steps)

animate_heatmap_section(density_grid_history_perfusion, concentration_grid_history_perfusion, time_steps)
animate_heatmap_section(density_grid_history_intervals, concentration_grid_history_intervals, time_steps)