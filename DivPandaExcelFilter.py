import pandas as pd 

df=pd.read_csv('Names.csv',header=None)
df.columns=['First','Last','Address','City','State','Area Code','Income']

df['Tax %'] = df['Income'].apply(lambda x: .20 if 10000<x<40000 else .30 if 40000<x<86000 else .35)
print(df)

df['TaxtoPay'] = df['Income'] * df['Tax %']
print(df['TaxtoPay'])
export=df.to_excel('ModifiedDivTax1.xlsx')
print('---------------------------------------')

todrop=['Address']
df.drop(columns=todrop, inplace=True)
print(df)

print('---------------------------------------')

df['Test Col'] = False
df.loc[df['Income'] < 60000, 'Test Col'] = True
print (df)