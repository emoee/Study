from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns
import warnings

diamond = sns.load_dataset('diamonds')
#print(diamond.keys())
'''
Index(['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'price', 'x', 'y',
       'z'],
      dtype='object')
'''

print(diamond['depth'].min())
print(diamond['carat'].agg(['mean','var']))
print(diamond[['x','y']].agg(['sum','std']))


penguin = sns.load_dataset('penguins')
#print(penguin.keys())
'''
Index(['species', 'island', 'bill_length_mm', 'bill_depth_mm',
       'flipper_length_mm', 'body_mass_g', 'sex'],
      dtype='object')
'''
print(penguin['species'].unique()) #고유값
print(penguin['island'].mode()) #최빈값
print(penguin['body_mass_g'].quantile(0.1)) #분위수
print(penguin['body_mass_g'].quantile(0.8)) #분위수