data = [(76.5, 43.5, 1288558), (76.5, 44.5, 429279), (76.5, 45.5, 858705), (76.5, 46.5, 1288635), 
        (77.5, 42.5, 1288458), (77.5, 43.5, 4386506), (77.5, 44.5, 15839894), (77.5, 45.5, 23389447), 
        (77.5, 46.5, 8160435), (77.5, 47.5, 1288497), (78.5, 41.5, 429392), (78.5, 42.5, 1717826), 
        (78.5, 43.5, 21853510), (78.5, 44.5, 82552974), (78.5, 45.5, 88274910), (78.5, 46.5, 19082788), 
        (78.5, 47.5, 3865416), (78.5, 48.5, 429642), (79.5, 42.5, 1861333), (79.5, 43.5, 29853891), 
        (79.5, 44.5, 123599631), (79.5, 45.5, 113251555), (79.5, 46.5, 33299005), (79.5, 47.5, 3670150), 
        (79.5, 48.5, 429393), (80.5, 42.5, 1718036), (80.5, 43.5, 10492117), (80.5, 44.5, 35844701), 
        (80.5, 45.5, 31129890), (80.5, 46.5, 8916696), (80.5, 47.5, 1288251), (81.5, 43.5, 2147723), 
        (81.5, 44.5, 2863957), (81.5, 45.5, 3240776), (81.5, 46.5, 429472), (82.5, 44.5, 429536)]

# Grouping by x and calculating the center of charge for y
grouped_data = {}
for x, y, charge in data:
    if x not in grouped_data:
        grouped_data[x] = {"sum_y_charge": 0, "sum_charge": 0}
    
    grouped_data[x]["sum_y_charge"] += y * charge
    grouped_data[x]["sum_charge"] += charge

result = [(x, values["sum_y_charge"]/values["sum_charge"]) for x, values in grouped_data.items()]

# Adding total charge to the result
result_with_charge = [(x, values["sum_y_charge"]/values["sum_charge"], values["sum_charge"]) for x, values in grouped_data.items()]

result_with_charge


print(result_with_charge)
