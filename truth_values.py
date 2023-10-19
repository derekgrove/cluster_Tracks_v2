import math

def calculate_true_beta(truth):
    local_start_x = truth[3]
    local_start_y = truth[4]
    local_end_x = truth[5]
    local_end_y = truth[6]
    
    delta_y = local_end_y - local_start_y
    delta_x = local_end_x - local_start_x
    
    # Calculate the angle in radians between the start and end points
    beta_rad = math.atan2(delta_y, delta_x)
    
    # Convert the angle to degrees
    beta_deg = math.degrees(beta_rad)
    
    # Normalize the angle to the range [0, 360)
    beta_deg = beta_deg % 360

    return beta_deg

def calculate_true_cluster_position(truth):
    cluster_position_x = truth[1]
    cluster_position_y = truth[2]
    
    return cluster_position_x, cluster_position_y

