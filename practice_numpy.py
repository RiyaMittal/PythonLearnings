import pandas as pd

import matplotlib.pyplot as plt

import xlrd

from matplotlib import style

style.use ( 'fivethirtyeight' )

country = pd.read_excel ( "C:\Users\mittariy\Desktop\panda_test_case.xlsx",
                        index_col=0 )

df = country.head ( 5 )

df = df.set_index ( ["country_code"] )

sd=df.reset_index()

print sd

"""

#sd= df.reset_index ([2010, 2011])

#print sd

db = df.diff ( axis=1 )

db.plot ( kind="bar" )

plt.show ()
"""