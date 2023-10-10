import parse_data as parse
from plotter import plot_weighted_data
from y_coc import * 
from fitting import fit_and_plot


def main():
    filename = 'raw_data.txt'
    truths, clusters = parse.parse_data(filename)

    # Calculate center of charge for each cluster
    #all_results = process_clusters(clusters)
    all_results = process_clusters_normalized(clusters)
    
    min_cluster = int(input("Enter the starting cluster index: "))
    max_cluster = int(input("Enter the ending cluster index: "))

    if min_cluster < 0 or max_cluster >= len(all_results):
        print("Error: Invalid cluster range. Please make sure the min and max are within the range of clusters.")
        return

    for i in range(min_cluster, max_cluster + 1):
        print(f"Plotting with fit for cluster {i}")
        # We're assuming here that plot_weighted_data expects a list of tuples, adjust as necessary.
        plot_weighted_data(all_results[i])
        print(all_results[i])
        fit_and_plot(all_results[i])

    #fit_and_plot(all_results)



if __name__ == "__main__":
    main()