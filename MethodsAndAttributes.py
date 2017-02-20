import pandas as pd

# Example 1
movies = pd.read_csv('http://bit.ly/imdbratings')
#print(movies.head())

#Output:

   # star_rating                     title content_rating   genre  duration  \
# 0          9.3  The Shawshank Redemption              R   Crime       142
# 1          9.2             The Godfather              R   Crime       175
# 2          9.1    The Godfather: Part II              R   Crime       200
# 3          9.0           The Dark Knight          PG-13  Action       152
# 4          8.9              Pulp Fiction              R   Crime       154
#
#                                          actors_list
# 0  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...
# 1    [u'Marlon Brando', u'Al Pacino', u'James Caan']
# 2  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...
# 3  [u'Christian Bale', u'Heath Ledger', u'Aaron E...
# 4  [u'John Travolta', u'Uma Thurman', u'Samuel L....

#describe
# print(movies.describe())

# Output

       # star_rating    duration
# count   979.000000  979.000000
# mean      7.889785  120.979571
# std       0.336069   26.218010
# min       7.400000   64.000000
# 25%       7.600000  102.000000
# 50%       7.800000  117.000000
# 75%       8.100000  134.000000
# max       9.300000  242.000000

#shape
# print(movies.shape)

# Output (rows, columns):
# (979, 6)

#dtypes
print(movies.dtypes)

#Output (data types):

# star_rating       float64
# title              object
# content_rating     object
# genre              object
# duration            int64
# actors_list        object
# dtype: object

# methods like describe are followed by a pair of parentheses
#attributes like shape do not need to be followed by parentheses