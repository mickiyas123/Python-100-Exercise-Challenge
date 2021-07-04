# Question: Create a script that uses the attached countries_by_area.txt  file as data source and prints out the top 5 most densely populated countries

# Expected output: 

# India
# Pakistan
# Nigeria
# China
# Indonesia



# import pandas as pd


# countries = pd.read_csv('countries_by_area.txt')

# countries.to_csv('countries_by_area.csv',index=None)

# countries = pd.read_csv('countries_by_area.csv', usecols=['country','population_2013'])
# countries = countries.sort_values('population_2013',ascending=False)
# print(countries.head())

import pandas as pd

data = pd.read_csv('countries_by_area.txt')
data['density'] = data['population_2013'] / data['area_sqkm']
data  =data.sort_values(by='density',ascending=False)
# print(data)
for index, row in data[:5].iterrows ():
    print(row["country"])

