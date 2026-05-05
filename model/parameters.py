class Parameters:
    def __init__(self):
        self.dt = 1/3600 # hours
        self.dx = 0.1 # mm
        self.diffusion_rate = 10 # mm^2/h
        self.EC50 = 0.5 # mM
        self.hill_coefficient = 1
        self.alpha = 0.1 # drug-induced death rate
        self.r = 0.05 # growth rate
        self.grid_dims = (100, 100, 100)
        self.source_position = (50, 50, 50)
        self.source_concentration = 0.001 # mM/h

def get_default_parameters():
    return Parameters()