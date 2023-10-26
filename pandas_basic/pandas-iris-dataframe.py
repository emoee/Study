from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns
import warnings

iris = sns.load_dataset('iris')
#iris.info()
'''
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   sepal_length  150 non-null    float64
 1   sepal_width   150 non-null    float64
 2   petal_length  150 non-null    float64
 3   petal_width   150 non-null    float64
 4   species       150 non-null    object 
dtypes: float64(4), object(1)
memory usage: 6.0+ KB

꽃받침 길이, 넓이, 꽃잎 길이, 넓이, 아이리스 종류
'''
iris['sepal'] = iris['sepal_length'] * iris['sepal_width']
#print(iris.head(5))
iris['petal'] = iris['petal_length'] * iris['petal_width']
#print(iris.head(5))
iris.drop(['petal_length', 'petal_width'], 1, inplace = True)
#print(iris.head(5))


print(iris.loc[iris['species'] == 'setosa'].sort_values('sepal', ascending=False).head(10))

print(iris['sepal'].mean() - iris['petal'].mean())