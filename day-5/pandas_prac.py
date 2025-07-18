import pandas as pd

s = pd.Series([10,20,30])
# print(s)

# data = {
#     "name":["Kshitish","Kumar","Pothal"],
#     'age':[25,30,35]
# }

# df = pd.DataFrame(data)
# print(df)

#read and write files
df = pd.read_csv('data_brick\day-5\Students.csv')
# Write to Excel
df.to_csv('output.csv',index=False)
# df = pd.read_csv('Orders.csv')
# df.to_csv('output.csv',index=False)
# print("Excel file 'output.csv' created successfully!")


#view and expolre data
df.head()
df.tail()
df.shape
print(df.info())
print(df.describe())
df.columns

#data selection
df['Name']
# df['Name','Age']
df.iloc[0]
df.loc[0,'Name']

# filter rows
print(df[df['Marks'] > 50])
df[(df['Marks'] > 50) & (df['Age'] < 80)]

#adding and modifying column
df['salary'] = [100,200,300,400,500,600,700,800,900,1001]
df['age in  5 years'] = df['Age'] + 5

# sorting and grouping
df.sort_values(by='Age', ascending=False)
df.groupby('Name')['Age'].mean()

# handeling mising data
df.isnull()
df.dropna()
df.fillna(0)
