import numpy as np
from iminuit import Minuit
import matplotlib.pyplot as plt

def line(x, a, b):
    return a * x + b


def fit_and_plot(result_with_charge):
    # Extracting data from result_with_charge
    x = np.array([item[0] for item in result_with_charge])
    y = np.array([item[1] for item in result_with_charge])
    weights = np.array([item[2] for item in result_with_charge])
    y_errors = np.array([item[3] for item in result_with_charge])
    

    # Chi-squared function
    def chi2(a, b):
        y_model = line(x, a, b)
        chi = (y - y_model) ** 2 / y_errors ** 2
        return np.sum(chi)

    # Minimize chi-squared
    m = Minuit(chi2, a=1, b=0)
    m.errordef = 1
    m.errors['a'] = 0.1
    m.errors['b'] = 0.1
    m.migrad()  # run the minimizer

    # Plotting
    plt.scatter(x, y, c='blue', marker='o', label='Data points', s=weights*100)  # scaling down the point size for clarity
    x_fit = np.linspace(min(x), max(x), 400)
    y_fit = line(x_fit, m.values['a'], m.values['b'])
    plt.xlim(min(x)-1, max(x)+1)
    plt.ylim(min(y)-1, max(y)+1)
    plt.plot(x_fit, y_fit, 'r-', label=f'Fit: y = ({m.values["a"]:.2f} +- {m.errors["a"]:.2f}) x + ({m.values["b"]:.2f}+- {m.errors["b"]:.2f})')
    plt.errorbar(x, y, yerr=y_errors, fmt='o', markersize=5, alpha=0.6, ecolor='red', capsize=3)
    print('chi square:', m.fval)
    print('errors in slope:', m.errors["a"])
    print('errors in y-intercept:', m.errors["b"])
    print('beta angle: ', angle_from_slope(a) )
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Weighted Linear Fit')
    plt.grid(True)
    plt.show()


#include these functions to get beta angle (angle of major axis) from the calculated slope:
def angle_from_slope(m):
    angle_rad = math.atan(m)
    angle_deg = math.degrees(angle_rad)
    return angle_deg

