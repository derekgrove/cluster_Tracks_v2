# line_fit_minimizer.py

import numpy as np
from iminuit import Minuit

def line(x, a, b):
    """Linear function: f(x) = a*x + b"""
    return a * x + b

def weighted_least_squares(params, x, y, weights):
    """Weighted least squares calculation."""
    a, b = params
    residuals = y - line(x, a, b)
    return np.sum(residuals**2 / weights)

def perform_minimization(x, y, weights):
    """Perform the minimization and return the best-fit parameters."""
    m = Minuit.from_array_func(weighted_least_squares, (0, 0), error=(0.1, 0.1), errordef=1, args=(x, y, weights), name=("a", "b"))
    m.migrad()
    return m.values['a'], m.values['b']

def fit_line_through_weighted_points(cluster):
    """Function to be called by analysis.py to fit a line through weighted points."""
    
    # Extract x, y, and weights (charge) from the cluster data
    x = np.array([pixel[0] + 0.5 for pixel in cluster])  # Adding 0.5 to center the data point in the pixel
    y = np.array([pixel[1] + 0.5 for pixel in cluster])  # Adding 0.5 to center the data point in the pixel
    weights = np.array([pixel[2] for pixel in cluster])
    
    # Perform the minimization
    a, b = perform_minimization(x, y, weights)
    
    return a, b
