def parse_data(filename):
    truths = []
    clusters = []

    with open(filename, 'r') as f:
        lines = f.read().split('\n')  # split the file content by new lines

        for line in lines:
            elements = line.split(', ')  # split each line by a comma + space
            if len(elements) >= 7:  # check if the line has at least 7 elements
                truths.append([float(e) for e in elements[:7]])  # add first 7 elements to the first list
                
                # Convert data to list of tuples (x, y, charge)
                cluster = [int(e) for e in elements[7:]]
                # Adjust the x and y values by adding 0.5 to center them in the pixel
                cluster = [(cluster[i] + 0.5, cluster[i+1] + 0.5, cluster[i+2]) for i in range(0, len(cluster), 3)]
                clusters.append(cluster)  # add the rest to the second list
            else: 
                continue
                
    return truths, clusters
