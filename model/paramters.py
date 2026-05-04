dt = 0.01 # hours
dx = 0.1 # mm

diffusion_rate = 0.01 # mm^2/h
EC50 = 0.5 # mM
hill_coefficient = 1
alpha = 0.1 # drug-induced death rate
r = 0.05 # growth rate

grid_dims = (100, 100, 100)
source_position = (50, 50, 50)
source_concentration = 0.01 # mM/h