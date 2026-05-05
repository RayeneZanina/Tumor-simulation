import numpy as np

class Parameters:
    def __init__(self):
        self.dt = 0.01 # hours
        self.dx = 0.2 # mm
        self.diffusion_rate = 0.25 # mm^2/h
        self.decay = 0.01 # 1/h
        self.beta = 0.05 # drug uptake rate, 1/h
        self.EC50 = 0.1 # mM
        self.hill_coefficient = 1.2
        self.alpha = 0.5 # drug-induced death rate
        self.r = 0.05 # growth rate
        self.movement_rate = 0.002 # cell movement rate, mm^2/h
        self.grid_dims = (40, 40, 40)
        self.source_positions = [[10,20,30],[10,20,30],[10,20,30]] # positions of drug sources
        self.source_concentration = 10 # mM/h
        self.dose = 5 # mM
        self.dose_interval = 0.5 # hours
        self.blob_centers = [(np.random.randint(10, 30), np.random.randint(10, 30), np.random.randint(10,30)) for _ in range(2)]
        self.blob_std_dev = 5 # mm

def get_default_parameters():
    return Parameters()