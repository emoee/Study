from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')
#print(tips.head())

#print(tips.sort_values(['total_bill', 'tip'], ascending=False).head(10))
#print(tips.sort_values(['size', 'tip'], ascending=[False, True]).head(10))

print(tips.loc[tips['day'].isin(['Fri','Sat']) & (tips['tip'] < 10), ['total_bill', 'tip', 'smoker', 'time']].head(10))

'''연습 문제'''
print(tips.pivot_table(index = 'smoker', columns = 'day', values = 'tip'))
print(tips.pivot_table(index = 'day', columns = 'time', values = 'total_bill', aggfunc = ['mean', 'sum']))