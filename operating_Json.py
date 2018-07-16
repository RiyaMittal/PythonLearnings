#!/usr/bin/python

import json
import csv

# = '{"employee_details":[{"employee_name": "James", "email": "james@gmail.com", "job_profile": "Sr. Developer"},{"employee_name": "Smith", "email": "Smith@gmail.com", "job_profile": "Project Lead"},.....]}'

#parsed_data=json.load('C:\Users\mittariy\PycharmProjects\Riya\employees.json')
#emp_data=parsed_data['Employees']

with open('C:\Users\mittariy\PycharmProjects\Riya\employees.json') as my_file:
    j_ob=json.load(my_file)

# open a file for writing

employ_data = open('C:\Users\mittariy\PycharmProjects\Riya\EmployData.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(employ_data)

count = 0

for emp in j_ob:

      if count == 0:

             header = emp.keys()

             csvwriter.writerow(header)

             count += 1

      csvwriter.writerow(emp.values())

employ_data.close()