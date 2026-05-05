class Parameters:
    def __init__(self):
        self.dt = 0.01 # hours
        self.dx = 0.2 # mm
        self.diffusion_rate = 0.1 # mm^2/h
        self.EC50 = 0.5 # mM
        self.hill_coefficient = 1
        self.alpha = 0.1 # drug-induced death rate
        self.r = 0.05 # growth rate
        self.grid_dims = (50, 50, 50)
        self.source_position = (25, 25, 25)
        self.source_concentration = 0.5 # mM/h
        self.dose = 0.5 # mM
        self.dose_interval = 0.5 # hours

def get_default_parameters():
    return Parameters()