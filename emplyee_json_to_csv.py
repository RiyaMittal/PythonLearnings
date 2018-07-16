import csv
import json

with open('C:\Users\mittariy\PycharmProjects\Riya\cake.json') as my_file:
    j_ob=json.load(my_file)

topping_dict=[]
batter_dict=[]

for items in j_ob["topping"]:
    #t_details=items
    topping_dict.append(items)

for items in j_ob["batters"]:
    #b_details=items
    batter_dict.append(items)

print topping_dict
print batter_dict

fields=['type','id']


# name of csv file
filename_1 = "topping_details11.csv"
filename_2 = "batter_details11.csv"

# writing to csv file
with open(filename_1, 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(topping_dict)

with open(filename_2, 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(batter_dict)


