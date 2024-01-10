#y center of charge calculation
import math
from numpy import *
import sys
def process_clusters(clusters, x_or_y):
    # This function will return a list of "center of charge" results for each cluster
    results = []
    
    for cluster in clusters:
        results.append(calculate_center_of_charge(cluster, x_or_y))
        
    return results

def cluster_center(cluster):
    total_charge = sum(charge for _, _, charge in cluster)

    xcharge = sum(x * charge for x, _, charge in cluster)
    ycharge = sum(y * charge for _, y, charge in cluster)

    x_coc = xcharge / total_charge
    y_coc = ycharge / total_charge

    cc = (x_coc, y_coc, total_charge)

    return cc

def calculate_center_of_charge(raw_data, x_or_y):
    # Calculate center of charge for each x value
    total_total_charge = sum([charge for _, _, charge in raw_data])

    grouped_data = {}
    #errors = 1/math.sqrt(12)
    #errors = 1
    if x_or_y == 'y':
        for x, y, charge in raw_data:
            if x not in grouped_data:
                grouped_data[x] = {"sum_y_charge": 0, "sum_charge": 0, "errors": 0}
        
            #error_y += math.sqrt(12) * charge 
            grouped_data[x]["sum_y_charge"] += y * charge
            #grouped_data[x]["y_errors"] += y_errors
            grouped_data[x]["sum_charge"] += charge
            #here, below, add a center of charge location instead of "45" I think
            #grouped_data[x]["errors"] += 45*charge/total_total_charge
            grouped_data[x]["errors"] += y*charge/total_total_charge
            
        result_with_charge = [(x, values["sum_y_charge"]/values["sum_charge"], values["sum_charge"], 1/values["errors"]) for x, values in grouped_data.items()]
        #result_with_charge = [(x - center_x, values["sum_y_charge"]/values["sum_charge"] - center_y, values["sum_charge"], 1/values["errors"]) for x, values in grouped_data.items()]
        #result_with_charge.append(1/math.sqrt(12)*charge)
        #print(result_with_charge)
        return result_with_charge

    if x_or_y == 'x':
        for x, y, charge in raw_data:
            if y not in grouped_data:
                grouped_data[y] = {"sum_x_charge": 0, "sum_charge": 0, "errors": 0}
        
            #error_y += math.sqrt(12) * charge 
            grouped_data[y]["sum_x_charge"] += x * charge
            #grouped_data[x]["y_errors"] += y_errors
            grouped_data[y]["sum_charge"] += charge
            grouped_data[y]["errors"] += 79*charge/total_total_charge
            

        result_with_charge = [(y, values["sum_x_charge"]/values["sum_charge"], values["sum_charge"], 1/values["errors"]) for y, values in grouped_data.items()]
        #result_with_charge.append(1/math.sqrt(12)*charge)
        #print(result_with_charge)
        return result_with_charge
    else:
        print("Error: Invalid value for x_or_y. Expected 'x' or 'y'.")
        sys.exit(1)


# we will also normalize the charge here, i.e. take each charged pixel and divide it by the total charge

#def process_clusters_normalized(cluster, x_or_y):
# This function will return a list of "center of charge" results for each cluster
# with normalized charges.
#    results = []
        #print(cluster)
        # Calculate total charge for the current cluster
#    total_charge = sum([charge for _, _, charge in cluster])
    
    # Normalize the charge for each pixel in the cluster
#    normalized_cluster = [(x, y, charge/total_charge) for x, y, charge in cluster]
    #print(normalized_cluster)
    
    # Calculate center of charge for the normalized cluster
#    coc_result = calculate_center_of_charge(normalized_cluster, x_or_y)
#    results.append(coc_result)
        
#    return results

def process_cluster_normalized(cluster, x_or_y):
    # Calculate total charge for the current cluster
    total_charge = sum([charge for _, _, charge in cluster])
    
    # Normalize the charge for each pixel in the cluster
    normalized_cluster = [(x, y, charge/total_charge) for x, y, charge in cluster]
    
    # Calculate center of charge for the normalized cluster
    coc_result = calculate_center_of_charge(normalized_cluster, x_or_y)
    
    return coc_result

def process_bulk_clusters_normalized(cluster, x_or_y):
# This function will return a list of "center of charge" results for each cluster
# with normalized charges.
   
    for cluster in cluster:
        # Calculate total charge for the current cluster
        total_charge = sum([charge for _, _, charge in cluster])
        
        # Normalize the charge for each pixel in the cluster
        normalized_cluster = [(x, y, charge/total_charge, 1/(math.sqrt(12)*charge)) for x, y, charge in cluster]

        
    return normalized_cluster