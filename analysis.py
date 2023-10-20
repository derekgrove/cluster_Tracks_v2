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
    x_or_y = input("x or y center of charge calculation? (y or x): ")
    # Calculate center of charge for each cluster
    #all_results = process_clusters(clusters)
    #all_results = process_bulk_clusters_normalized(clusters)
    all_results = process_clusters_normalized(clusters, x_or_y)
    #all_results_2 = process_bulk_clusters_normalized
    beta_values = []
    #print(all_results)
    
    
    #implement below

    if min_cluster < 0 or max_cluster >= len(all_results):
        print("Error: Invalid cluster range. Please make sure the min and max are within the range of clusters.")
        return

    for i in range(min_cluster, max_cluster + 1):
        print(f"Plotting with fit for cluster {i}")
        # We're assuming here that plot_weighted_data expects a list of tuples, adjust as necessary.
        #plot_weighted_data(all_results[i], i)
        #print(all_results[i])
        m, weights, x, y, errors, calculated_beta = iminuit_chi2(all_results[i])
        if make_plots:
            plot_imin_obj(m, weights, x, y, errors, calculated_beta, i, x_or_y)
        #plot_weighted_data_with_fit(all_results_2[i], i, m)
        true_beta = calculate_true_beta(truths[i])
        beta_values.append((calculated_beta, true_beta))
        
    
    differences = [true - calculated for calculated, true in beta_values]
    if make_hist:
        plot_histogram(differences, 'Difference (beta_true - beta_calculated)', '(beta_true - beta_calculated)')
        plot_histogram([item[0] for item in beta_values], 'Calculated Betas from minuit', 'Beta (degrees)')
        plot_histogram([item[1] for item in beta_values], 'Truth Betas from allpix', 'Beta (degrees)')

        



if __name__ == "__main__":
    main()