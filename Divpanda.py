import pandas as pd 
from openpyxl.workbook import workbook


#df_excel=pd.read_excel('Divexcel.xlsx')

#print(df_excel)

print('----------------------------------------------')

df=pd.read_csv('Names.csv', header=None)
df.columns=['First','Last','Address','City','State','Area Code','salary']
#df.to_excel('modified.xlsx') # changes to csv to excel file
#df.to_html('csvtohtml.html')
#df.to_json('csvtojson.txt')

print(df['Last']) # print only one column value
print(df[['State','salary']]) # print any2 column value
print(df['First'][0:3]) # print First columns 3 rows only
print(df.iloc[1]) # print column name and 1st row value in dict
print(df.iloc[2,1]) # print column name and 1st row value in dict

print(df.loc[df['City']=='Riverside']) # to filter column city with value riverside
print(df.loc[(df['City']=='Riverside') & (df['First']=='John')])


#wantedval=df[['First','Last','State']]
#Stored=wantedval.to_excel('modifiednew.xlsx', index=None) # only 3 column value in new excel



print('----------------------------------------------')

#df_txt=pd.read_csv('Divtxt.txt', delimiter='\t')

#print(df_txt)

