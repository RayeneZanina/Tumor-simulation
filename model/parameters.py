class Parameters:
    def __init__(self):
        self.dt = 0.01 # hours
        self.dx = 0.2 # mm
        self.diffusion_rate = 0.2 # mm^2/h
        self.decay = 0.005 # 1/h
        self.beta = 0.05 # drug uptake rate, 1/h
        self.EC50 = 0.5 # mM
        self.hill_coefficient = 1.2
        self.alpha = 1.5 # drug-induced death rate
        self.r = 0.05 # growth rate
        self.movement_rate = 0.002 # cell movement rate, mm^2/h
        self.grid_dims = (40, 40, 40)
        self.source_position = (20, 20, 20)
        self.source_concentration = 10 # mM/h
        self.dose = 5 # mM
        self.dose_interval = 0.25 # hours

def get_default_parameters():
    return Parameters()