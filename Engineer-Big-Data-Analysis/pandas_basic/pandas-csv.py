from IPython.display import Image
import numpy as np
import pandas as pd

df = pd.read_csv('data/seoul_population.csv')
df = pd.read_csv('data/seoul_population.csv')
df.to_csv('./sample_file/sample2.csv', index=False)

'''
#엑셀도 csv로 저장 가능
excel = pd.read_excel('data/seoul_transportation.xlsx', sheet_name='버스', engine='openpyxl')
excel.head()
excel.to_csv('./sample_file/sample1.csv', index=False)
'''

sample = pd.read_excel('data/판다스입출력샘플/file_sample.xlsx', sheet_name=None, engine='openpyxl')
print(sample.keys())

sample_2010 = sample['2020년 10월']
print(sample_2010)

sample_2010.to_csv('./sample_file/2020-10-oil-price.csv',index=False)