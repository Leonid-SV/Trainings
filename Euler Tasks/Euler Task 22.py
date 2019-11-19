import numpy
import pandas
from pprint import pprint

pd = pandas.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine']}, index= ['kz', 'ru', 'bl', 'uk'])

print(pd['country'])
print(pd.iloc[0])

pd['population'] = [17.04, 143.5, 9.5, 45.5]
pd.index.name = 'Country Code'
print('******************** \n')
print(pd.loc['ru'])

