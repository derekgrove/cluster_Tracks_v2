#y center of charge calculation
import math
from numpy import *
def process_clusters(clusters):
    # This function will return a list of "center of charge" results for each cluster
    results = []
    
    for cluster in clusters:
        results.append(calculate_center_of_charge_y(cluster))
        
    return results

def calculate_center_of_charge_y(raw_data):
    # Calculate center of charge for each x value
    grouped_data = {}
    y_errors = 1/math.sqrt(12)
    for x, y, charge in raw_data:
        if x not in grouped_data:
            grouped_data[x] = {"sum_y_charge": 0, "sum_charge": 0, "y_errors": y_errors}
    
        #error_y += math.sqrt(12) * charge 
        grouped_data[x]["sum_y_charge"] += y * charge
        #grouped_data[x]["y_errors"] += y_errors
        grouped_data[x]["sum_charge"] += charge
        

    result_with_charge = [(x, values["sum_y_charge"]/values["sum_charge"], values["sum_charge"], values["y_errors"]) for x, values in grouped_data.items()]
    #result_with_charge.append(1/math.sqrt(12)*charge)
    #print(result_with_charge)
    return result_with_charge

# we will also normalize the charge here, i.e. take each charged pixel and divide it by the total charge

def process_clusters_normalized_y(clusters):
# This function will return a list of "center of charge" results for each cluster
# with normalized charges.
    results = []

    for cluster in clusters:
        #print(cluster)
        # Calculate total charge for the current cluster
        total_charge = sum([charge for _, _, charge in cluster])
        
        # Normalize the charge for each pixel in the cluster
        normalized_cluster = [(x, y, charge/total_charge) for x, y, charge in cluster]
        #print(normalized_cluster)
        
        # Calculate center of charge for the normalized cluster
        coc_result = calculate_center_of_charge(normalized_cluster)
        results.append(coc_result)
        
    return results

def process_bulk_clusters_normalized(clusters):
# This function will return a list of "center of charge" results for each cluster
# with normalized charges.
    results = []

    for cluster in clusters:
        # Calculate total charge for the current cluster
        total_charge = sum([charge for _, _, charge in cluster])
        
        # Normalize the charge for each pixel in the cluster
        normalized_cluster = [(x, y, charge/total_charge, 1/(math.sqrt(12)*charge)) for x, y, charge in cluster]

        
        # bypass the center of charge calculation, pass normalized cluster right back to program
        # this is done at Alice's request so we can see the pixelated data and fit lines to it
        results.append(normalized_cluster)
        #print(results)
        
    return results