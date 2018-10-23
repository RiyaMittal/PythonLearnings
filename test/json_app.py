import os
import json


def print_json_data(data_d,data_type,data_col):
	print("\n Here is the listing of {}".format(data_type))
	for items in data_d:
		print(items[data_col])
		
		
		
working_dir='test'
file_name='json_data.json'
#new_file_name='new_customer.csv'
my_file=os.path.join('C:\\test',file_name)
#my_new_file=os.path.join('C:\\test',new_file_name)

# load data from json file

user_data=open(my_file)
json_handler=json.load(user_data)
print(type(json_handler[0]))
print(type(json_handler))
print_json_data(json_handler,'users','last_name')
user_data.close()



