import pandas as pd
import numpy as np
from sklearn import preprocessing

#load the data
train=pd.read_csv("C:/ML/train.csv")

test=pd.read_csv("C:/ML/test.csv")

train.info()  #check data set

print ("train data info:(row,column) ",train.shape) # this will return number of rows and columns
print ("test data info:(row,column) ",test.shape) # this will return number of rows and columns

print train.head()

# to check the missing values in the data:

print train.shape[0] # it returns the number of rows in the data

nans_train=train.shape[0]-train.dropna().shape[0]
print("%d rows have missing values in the train data "%nans_train)

print test.shape[0]

nans_test=test.shape[0]-test.dropna().shape[0]
print("%d rows have missing values in the test data "%nans_test)

# now find out which column has the missing values??????????????????????????

print train.isnull() # it returns TRUE if the field is null

print train.isnull().sum() # it returns total number of null in the data

cat = train.select_dtypes(include=['O']) #Let's count the number of unique values from character variables.
#print cat
cat.apply(pd.Series.nunique)

# so we now know that the missing values are in 3 character variables:
#workclass
#occupation
#native.country

#let's impute these missing values with their respective modes.

train.workclass.value_counts(sort=True)# value_counts method will return the number of distinct values held by the column specified. sort=Tru will sort the value list
train.workclass.fillna('Private',inplace=True)#  fillna method will fill all the NaN fields with the one specified and inplace means we are placing it in that place

train.occupation.value_counts(sort=True)
train.occupation.fillna('Prof-specialty',inplace=True)

train['native.country'].value_counts(sort=True)
train['native.country'].fillna('United-States',inplace=True)

# check again for missing values:

print train.isnull().sum()

#Now, we'll check the target variable to investigate if this data is imbalanced or not.

print train.target.value_counts()/train.shape[0]

#print train.target.value_counts()

#We see that 75% of the data set belongs to <=50K class.
# This means that even if we take a rough guess of target prediction as <=50K, we'll get 75% accuracy.

print pd.crosstab(train.education, train.target, margins=True)/train.shape[0]

#Scikit learn accepts data in numeric format. Now, we'll have to convert the character variable into numeric. We'll use the labelencoder function.

#In label encoding, each unique value of a variable gets assigned a number, i.e., let's say a variable color has four values ['red','green','blue','pink'].

for x in train.columns:
    if train[x].dtype== 'object':
        lbl=preprocessing.LabelEncoder()
        lbl.fit(list(train[x].values))
        train[x]=lbl.transform(list(train[x].values))

print train.head()

#As we can see, all the variables have been converted to numeric, including the target variable.

#<50K = 0 and >50K = 1

print train.target.value_counts()