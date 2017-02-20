import pandas as pd

# Example 1
# ufo = pd.read_table('http://bit.ly/uforeports', sep=',')
ufo = pd.read_csv('http://bit.ly/uforeports')

#for some reason I am unable to access this data so I will simply copy the commands used in this example

# This is a Data Frame
# print(ufo.head())
# print(type(ufo))

# This is a Series within a Data Frame
# print(ufo['City'])
# print(type(ufo['City'])
# print(ufo.City)

# Bracket notation must be used if the Series name contains a space
# print(ufo['Colors Reported'])

# There are certain circumstances where dot notation will not work, but bracket notation will always work.

# ufo['Location'] = ufo.City + ', ' + ufo.State
# will result in the series ufo.Location formatted (City, State)
#new series must be written in bracket notation