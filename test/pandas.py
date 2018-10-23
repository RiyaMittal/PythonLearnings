import pandas as pd
from sklearn.datasets import load_boston
dataset1=load_boston()
print(dataset1.data)

dfX=pd.DataFrame(dataset1.data,columns=dataset1.feature_names)
dfY=pd.DataFrame(dataset1.target)
print(dfX.shape)
print(dfY.shape)
