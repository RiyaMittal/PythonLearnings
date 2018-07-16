import pandas as pd

# this program is to understand the concept of categorzing the continuous variables
#Understand the output - '(' means the value is included in the bin, '[' means the value is excluded

ages = [20, 22, 45, 27, 21, 23, 37, 31, 61, 45, 41, 32]


bins=[18,25,35,60,100]
bin_names=['A','B','C','D','E']
cats=pd.cut(ages,bins)
print cats
print cats.codes
print  pd.value_counts(cats)

#To include the right bin value, we can do:
cats1=pd.cut(ages,bins,right=False)
print cats1
print cats1.codes
#print  pd.value_counts(cats1)
print  pd.value_counts(cats1).cumsum()


#new_cats=pd.cut(ages,bins,code=bin_names)
#print new_cats