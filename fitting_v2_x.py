import math
import numpy as np
from iminuit import Minuit
import matplotlib.pyplot as plt

def x_line(y, c, d):
    return c * y + d


def iminuit_chi2_x(result_with_charge):
    #print("result_with_charge:")
    #print(result_with_charge)
    # Extracting data from result_with_charge
    y = np.array([item[0] for item in result_with_charge])
    x = np.array([item[1] for item in result_with_charge])
    weights = np.array([item[2] for item in result_with_charge])
    errors = np.array([item[3] for item in result_with_charge])
    #y_errors[3] = y_errors[3]*.1
    #y_errors[0] = y_errors[0]*10
    #y_errors[6] = y_errors[6]*10
    #print("errors:")
    #print(errors)
    #print("x:")
    #print(x)
    
    # Chi-squared function
    def chi2(c, d):
        x_model = x_line(y, c, d)
        chi = (x - x_model) ** 2 / errors**2
        return np.sum(chi)

    # Minimize chi-squared
    m = Minuit(chi2, c=1, d=0)
    m.errordef = 1
    m.errors['c'] = 0.1
    m.errors['d'] = 0.1
    m.migrad()  # run the minimizer
    beta_angle = angle_from_slope_x(m.values['c'])
    print("m.values['c']:")
    print(m.values['c'])
    return m, weights, x, y, errors, beta_angle
    
'''def plot_imin_obj_x(m, weights, x, y, errors, calc_beta, true_beta, i):
    # Plotting
    plt.scatter(y, x, c='blue', marker='o', label='Data points', s=weights*100)  # scaling down the point size for clarity
    y_fit = np.linspace(min(y), max(y), 400)
    x_fit = x_line(y_fit, m.values['c'], m.values['d'])
    dof = len(x) - 2  # degrees of freedom = number of data points - number of fitted parameters
    reduced_chi2 = m.fval / dof
    print('reduced chi square:', reduced_chi2)
    plt.xlim(min(x)-1, max(x)+1)
    plt.ylim(min(y)-1, max(y)+1)
    plt.plot(y_fit, x_fit, 'r-', label=f'Fit: y = ({m.values["c"]:.2f} +- {m.errors["c"]:.2f}) x + ({m.values["d"]:.2f}+- {m.errors["d"]:.2f})')
    plt.errorbar(x, y, xerr=errors, fmt='o', markersize=5, alpha=0.6, ecolor='blue', capsize=3)
    #print(y_errors)
    #print(1/(math.sqrt(12)))
    #point1, point2 = true_beta_line
    # Plot the true beta line
    #plt.plot([point1[0], point2[0]], [point1[1], point2[1]], 'g--', label='True Beta Line')

    
    beta_calc_text = f"Calc Beta Angle: {calc_beta:.2f}°"
    beta_true_text = f"True Beta Angle: {true_beta:.2f}°"
    #x_position = min(x) + 0.9 * (max(x) - min(x))  # 10% from the left edge
    #y_position = max(y) + 0.9 * (max(y) - min(y))  # 10% from the top edge
    plt.text(1, 0, beta_calc_text, 
            fontsize=10, 
            transform=plt.gca().transAxes, 
            horizontalalignment='right', 
            verticalalignment='bottom', 
            bbox=dict(facecolor='white', alpha=0.5, pad=5))
    plt.text(1, 0.1, beta_true_text, 
            fontsize=10, 
            transform=plt.gca().transAxes, 
            horizontalalignment='right', 
            verticalalignment='bottom', 
            bbox=dict(facecolor='white', alpha=0.5, pad=5))
    #print('chi square:', m.fval)
    print('errors in slope:', m.errors["c"])
    print('errors in y-intercept:', m.errors["d"])
    print('beta angle from iminuit: ', angle_from_slope_x(m.values['c']))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Weighted Linear Fit Cluster ' + str(i))
    plt.grid(True)
    plt.show()'''

'''def plot_imin_obj_x(m, weights, x, y, errors, calc_beta, true_beta, i):
    # Plotting
    plt.scatter(y, x, c='blue', marker='o', label='Data points', s=weights*100)  # Note the swap of x and y

    # Fit line calculation needs to be adjusted for x as dependent variable
    y_fit = np.linspace(min(y), max(y), 400)
    print("y:")
    print(y)
    print("min y:")
    print(min(y))
    print("max y:")
    print(max(y))
    x_fit = x_line(y_fit, m.values['c'], m.values['d'])
    dof = len(y) - 2  # degrees of freedom = number of data points - number of fitted parameters
    reduced_chi2 = m.fval / dof
    print('reduced chi square:', reduced_chi2)
    #plt.ylim(min(x)-1, max(x)+1)  # Note the change to ylim for x range
    #plt.xlim(min(y)-1, max(y)+1)  # And xlim for y range
    plt.ylim(0, 100)  # Note the change to ylim for x range
    plt.xlim(0, 100)  # And xlim for y range

    #line below is responsible for calculating the calculated beta line
    plt.plot(x_fit, y_fit, 'r-', label=f'Fit: x = ({m.values["c"]:.2f} +- {m.errors["c"]:.2f}) y + ({m.values["d"]:.2f} +- {m.errors["d"]:.2f})')

    # Adding x-error bars
    plt.errorbar(y, x, xerr=errors, fmt='o', markersize=5, alpha=0.6, ecolor='blue', capsize=3)

    beta_calc_text = f"Calc Beta Angle: {calc_beta:.2f}°"
    beta_true_text = f"True Beta Angle: {true_beta:.2f}°"
    plt.text(1, 0, beta_calc_text, 
            fontsize=10, 
            transform=plt.gca().transAxes, 
            horizontalalignment='right', 
            verticalalignment='bottom', 
            bbox=dict(facecolor='white', alpha=0.5, pad=5))
    plt.text(1, 0.1, beta_true_text, 
            fontsize=10, 
            transform=plt.gca().transAxes, 
            horizontalalignment='right', 
            verticalalignment='bottom', 
            bbox=dict(facecolor='white', alpha=0.5, pad=5))

    print('errors in slope:', m.errors["c"])
    print('errors in y-intercept:', m.errors["d"])
    print('beta angle from iminuit: ', angle_from_slope_x(m.values['c']))

    plt.ylabel('Y')  
    plt.xlabel('X')
    plt.legend()
    plt.title('Weighted Linear Fit Cluster ' + str(i))
    plt.grid(True)
    plt.show()'''

def plot_imin_obj_x(m, weights, x, y, errors, calc_beta, true_beta, i):
    # Plotting
    plt.scatter(x, y, c='blue', marker='o', label='Data points', s=weights*100)  # scaling down the point size for clarity
    y_fit = np.linspace(min(y), max(y), 400)
    #print("yfit:")
    #print(y_fit)
    x_fit = x_line(y_fit, m.values['c'], m.values['d'])
    #print("xfit:")
    #print(x_fit)
    dof = len(x) - 2  # degrees of freedom = number of data points - number of fitted parameters
    reduced_chi2 = m.fval / dof
    print('reduced chi square:', reduced_chi2)
    plt.xlim(min(x)-1, max(x)+1)
    plt.ylim(min(y)-1, max(y)+1)
    #plt.xlim(0, 100)
    #plt.ylim(0, 100)

    plt.plot(y_fit, x_fit, 'r-', label=f'Fit: y = ({m.values["c"]:.2f} +- {m.errors["c"]:.2f}) x + ({m.values["d"]:.2f}+- {m.errors["d"]:.2f})')
    plt.errorbar(x, y, xerr=errors, fmt='o', markersize=5, alpha=0.6, ecolor='blue', capsize=3)
    #print(y_errors)
    #print(1/(math.sqrt(12)))
    #point1, point2 = true_beta_line
    # Plot the true beta line
    #plt.plot([point1[0], point2[0]], [point1[1], point2[1]], 'g--', label='True Beta Line')

    
    beta_calc_text = f"Calc Beta Angle: {calc_beta:.2f}°"
    beta_true_text = f"True Beta Angle: {true_beta:.2f}°"
    #x_position = min(x) + 0.9 * (max(x) - min(x))  # 10% from the left edge
    #y_position = max(y) + 0.9 * (max(y) - min(y))  # 10% from the top edge
    plt.text(1, 0, beta_calc_text, 
            fontsize=10, 
            transform=plt.gca().transAxes, 
            horizontalalignment='right', 
            verticalalignment='bottom', 
            bbox=dict(facecolor='white', alpha=0.5, pad=5))
    plt.text(1, 0.1, beta_true_text, 
            fontsize=10, 
            transform=plt.gca().transAxes, 
            horizontalalignment='right', 
            verticalalignment='bottom', 
            bbox=dict(facecolor='white', alpha=0.5, pad=5))
    #print('chi square:', m.fval)
    print('errors in slope:', m.errors["c"])
    print('errors in y-intercept:', m.errors["d"])
    print('beta angle from iminuit: ', angle_from_slope_x(m.values['c']))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Weighted Linear Fit Cluster ' + str(i))
    plt.grid(True)
    plt.show()



#include these functions to get beta angle (angle of major axis) from the calculated slope:
def angle_from_slope_x(m):
    angle_rad = math.atan(m)
    angle_deg = math.degrees(angle_rad)
    return angle_deg
