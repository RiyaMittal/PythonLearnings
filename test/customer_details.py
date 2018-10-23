import os
import csv


def print_list(list_data,list_type):
	print("\n Here is the listing of {}".format(list_type))
	for items in list_data:
		print(items)
		
		
		
working_dir='test'
file_name='customer.csv'
new_file_name='new_customer.csv'
my_file=os.path.join('C:\\test',file_name)
my_new_file=os.path.join('C:\\test',new_file_name)

# read from a csv file

customer_file=open(my_file)
customer_reader=csv.reader(customer_file)
customer_data=list(customer_reader)

print("\n passing the reader to the list() to create list of lists:")

print(customer_data)
print_list(customer_data,'customers')
print(customer_data[1][1]+ 'email' + customer_data[1][2])

customer_file.close()

# write to a csv file
customer_file=open(my_new_file,'a')
customer_writer=csv.writer(customer_file)
customer_writer.writerow(['customer_id','customer_name','customer_email'])
customer_writer.writerow(['2','Prachi1','prachi1@hpe.com'])

print("\n successfully created a new csv file")
customer_file.close()

