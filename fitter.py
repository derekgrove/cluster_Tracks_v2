import numpy as np
from iminuit import Minuit
import matplotlib.pyplot as plt

def line(x, a, b):
    return a * x + b

def chi2(a, b, x, y, weights):
    y_model = line(x, a, b)
    chi = (y - y_model) ** 2 * weights
    return np.sum(chi)

def fit_and_plot(cluster):
    x = np.array([point[0] for point in cluster])
    y = np.array([point[1] for point in cluster])
    weights = np.array([point[2] for point in cluster])

    # Bind x, y, and weights to the chi2 function using a lambda
    chi2_to_minimize = lambda a, b: chi2(a, b, x, y, weights)

    m = Minuit(chi2_to_minimize, a=1, b=0, a_error=0.1, b_error=0.1, errordef=1, pedantic=False)
    m.migrad()

    plt.scatter(x, y, c='blue', marker='o', label='Data points', s=weights*0.00001)
    x_fit = np.linspace(min(x), max(x), 400)
    y_fit = line(x_fit, m.values['a'], m.values['b'])
    plt.plot(x_fit, y_fit, 'r-', label=f'Fit: y = {m.values["a"]:.2f}x + {m.values["b"]:.2f}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Weighted Linear Fit')
    plt.grid(True)
    plt.show()
