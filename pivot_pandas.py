import pandas as pd
import numpy as np


df=pd.DataFrame({'key1':['a','a','b','b','a'],'key2':['one','two','one','two','one'],'data1':np.random.rand(5),'data2':np.random.rand(5)})
print df

grouped=df['data1'].groupby(df['key1'])

print grouped.mean()

#print df['data1']

# to slice

dates=pd.date_range('20180401',periods=6)
#print dates

#dfdate=pd.DataFrame({'key1':['a','b','c','d','e'],'key2':['One','Two','Three','Four','Five'],'data1':np.random.rand(6),'data2':np.random.rand(6)},index=dates)

#dfdate=pd.DataFrame(np.random.rand(4,6),index=dates,columns=list('ABCD'))
dfdate=pd.DataFrame(np.random.rand(6,4),index=dates,columns=list('ABCD'))
print dfdate
#print dfdate['20180401':'20180403']
#print dfdate.loc[:,['B','C']]
#print dfdate.loc['20180402':'20180403',['B','C']]
#print dfdate.iloc[3] # returns 3rd row( 3rd index)

print dfdate.iloc[2:4, 0:2] # returns a specific number of rows

print dfdate.iloc[[1,5],[0,2]] # returns the data based on column and row needed

print dfdate[dfdate.A>0.7]

dfdate2= dfdate.copy() # to copy
print dfdate2
dfdate2['EE']=['one','two','three','four','five','six'] ## adding new column
print dfdate2

print dfdate.query('A>B')


print df.pivot_table(values='data1',index='key1',aggfunc='count')# pivot table count

print df.pivot_table(values='data1',index='key1',aggfunc=np.mean) # pivot table mean
