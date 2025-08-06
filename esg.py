import numpy as np

class StochasticRateESG:
    def __init__(self, base_rate):
        self.base_rate = base_rate
    
    def generate(self, num_paths, num_years):
        base_rate_matrix = np.full((num_paths, num_years), self.base_rate) # Generates a matrix of size (paths , years), with all the values being the base_rate

        # The following line creates a matrix with each value being derived randomly from a Normal (Gaussian) Distribution
        # loc is the mean of the distribution, scale is the standard deviation of the distribution, and size is the dimensions of the matrix
        noise = np.random.normal(loc=0.0, scale=0.03, size=(num_paths, num_years)) 
        return base_rate_matrix + noise # Add the values from the noise to our base rate to get randomly varying interest rates
