import parse_data as parse
from plotter import *
from coc import * 
from fitting_v2 import *
from truth_values import *


def main():
    filename = 'raw_data.txt'
    truths, clusters = parse.parse_data(filename)

    min_cluster = int(input("Enter the starting cluster index: "))
    max_cluster = int(input("Enter the ending cluster index: "))
    make_plots = input("Make plots? (yes, no): ").lower() == "yes"
    make_hist = input("Make histogram of beta differences? (yes, no): ").lower() == "yes"
    # Calculate center of charge for each cluster
    #all_results_bulk = process_clusters(clusters)
    #x_center, y_center, total_charge = cluster_center(clusters)
    

    #all_results_2 = process_bulk_clusters_normalized
    beta_values = []
    #print(all_results)
    #charge for _, _, charge in cluster
    
    #implement below

    if min_cluster < 0 or max_cluster >= len(clusters):
        print("Error: Invalid cluster range. Please make sure the min and max are within the range of clusters.")
        return

    for i in range(min_cluster, max_cluster + 1):
        print(f"Plotting with fit for cluster {i}")
        # We're assuming here that plot_weighted_data expects a list of tuples, adjust as necessary.
        #plot_weighted_data(all_results_bulk[i], i)
        #print(all_results[i])
        x_center, y_center, total_charge = cluster_center(clusters[i])
        coc_result = process_cluster_normalized(clusters[i])
        adjusted_cluster = [(x - x_center, y - y_center, charge, error) for x, y, charge, error in coc_result]
        print("x_center: " + str(x_center))
        print("y_center: " + str(y_center))
        m, weights, x, y, errors, calculated_beta = iminuit_chi2(adjusted_cluster)
        true_beta = calculate_true_beta(truths[i])
        print("true beta: " + str(true_beta))
        #true_beta_line = calculate_line_points(x_center, y_center, true_beta)
        #print(true_beta_line)

        beta_values.append((calculated_beta, true_beta))
        if make_plots:
            plot_imin_obj(m, weights, x, y, errors, calculated_beta, true_beta, i)
        #plot_weighted_data_with_fit(all_results_2[i], i, m)
        
        
    
    differences = [true - calculated for calculated, true in beta_values]
    if make_hist:
        plot_histogram(differences, 'Difference (beta_true - beta_calculated)', '(beta_true - beta_calculated)')
        plot_histogram([item[0] for item in beta_values], 'Calculated Betas from minuit', 'Beta (degrees)')
        plot_histogram([item[1] for item in beta_values], 'Truth Betas from allpix', 'Beta (degrees)')
        
    #print(beta_values)
    #normal_plot(beta_values, "true beta vs calculated beta (x center of charge)", "calculated beta (degrees)", "true beta (degrees)")

        



if __name__ == "__main__":
    main()