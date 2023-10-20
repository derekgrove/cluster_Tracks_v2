import math
import numpy as np
from iminuit import Minuit
import matplotlib.pyplot as plt

def line(x, a, b):
    return a * x + b


def iminuit_chi2(result_with_charge):
    # Extracting data from result_with_charge
    x = np.array([item[0] for item in result_with_charge])
    y = np.array([item[1] for item in result_with_charge])
    weights = np.array([item[2] for item in result_with_charge])
    y_errors = np.array([item[3] for item in result_with_charge])
    #print("y_errors:")
    #print(y_errors)
    

    # Chi-squared function
    def chi2(a, b):
        y_model = line(x, a, b)
        chi = (y - y_model) ** 2 / y_errors**2
        return np.sum(chi)

    # Minimize chi-squared
    m = Minuit(chi2, a=1, b=0)
    m.errordef = 1
    m.errors['a'] = 0.1
    m.errors['b'] = 0.1
    m.migrad()  # run the minimizer
    beta_angle = angle_from_slope(m.values['a'])
    return m, weights, x, y, y_errors, beta_angle

def plot_imin_obj(m, weights, x, y, errors, beta_angle, i, x_or_y):
    # Plotting
    plt.scatter(x, y, c='blue', marker='o', label='Data points', s=weights*100)  # scaling down the point size for clarity
    x_fit = np.linspace(min(x), max(x), 400)
    y_fit = line(x_fit, m.values['a'], m.values['b'])
    dof = len(x) - 2  # degrees of freedom = number of data points - number of fitted parameters
    reduced_chi2 = m.fval / dof
    print('reduced chi square:', reduced_chi2)
    plt.xlim(min(x)-1, max(x)+1)
    plt.ylim(min(y)-1, max(y)+1)
    plt.plot(x_fit, y_fit, 'r-', label=f'Fit: y = ({m.values["a"]:.2f} +- {m.errors["a"]:.2f}) x + ({m.values["b"]:.2f}+- {m.errors["b"]:.2f})')
    plt.errorbar(x, y, yerr=errors, fmt='o', markersize=5, alpha=0.6, ecolor='red', capsize=3)
    #print(y_errors)
    #print(1/(math.sqrt(12)))
    
    angle_text = f"Beta Angle: {beta_angle:.2f}°"
    #x_position = min(x) + 0.9 * (max(x) - min(x))  # 10% from the left edge
    #y_position = max(y) + 0.9 * (max(y) - min(y))  # 10% from the top edge
    plt.text(1, 0, angle_text, 
            fontsize=10, 
            transform=plt.gca().transAxes, 
            horizontalalignment='right', 
            verticalalignment='bottom', 
            bbox=dict(facecolor='white', alpha=0.5, pad=5))
    #print('chi square:', m.fval)
    print('errors in slope:', m.errors["a"])
    print('errors in y-intercept:', m.errors["b"])
    print('beta angle from iminuit: ', angle_from_slope(m.values['a']))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Weighted Linear Fit Cluster ' + str(i))
    plt.grid(True)
    plt.show()


#include these functions to get beta angle (angle of major axis) from the calculated slope:
def angle_from_slope(m):
    angle_rad = math.atan(m)
    angle_deg = math.degrees(angle_rad)
    return angle_deg
