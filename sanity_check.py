import parse_data as parse

def main():
    filename = 'raw_data.txt'
    truths, clusters = parse.parse_data(filename)
    #print("truths is: ")
    #print(truths)
    #print("clusters is: ")
    #print(clusters)
    min_cluster = int(input("Enter the starting cluster index: "))
    max_cluster = int(input("Enter the ending cluster index: "))

    for i in range(min_cluster, max_cluster + 1):
        total_charge = sum([charge for _, _, charge in clusters[i]])
        print("total charge for cluster " + str(i) + ": ")
        print(total_charge)
        
        return
if __name__ == "__main__":
    main()