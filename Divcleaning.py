import pandas as pd 
import numpy as np 

from openpyxl.workbook import workbook

df=pd.read_csv('Names.csv', header=None)
df.columns=['First','Last','Address','City','State','Area Code','Income']

df.drop(columns='Address', inplace=True)
df= df.set_index('Area Code')

print(df.loc[8074]) # retrieves row with 8074 as area code

print(df.First.str.split(expand=True)) # first name has 3 words, so splitting first name as 3 columns

df.First=df.First.str.split(expand=True) # gets only first name's first word only
print(df.First)

df=df.replace(np.nan, 'N/A',regex=True)
export=df.to_excel('ModifiedDivClean.xlsx')


