import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')
ufo.columns = ufo.columns.str.replace(' ', '_')
columns = ufo.columns
print(columns)

#Output:
# Index(['City', 'Colors_Reported', 'Shape_Reported', 'State', 'Time'], dtype='object')

# Example 1
ufo.drop('Colors_Reported', axis=1, inplace=True)
columns = ufo.columns
print(columns)

# Output:
# Index(['City', 'Shape_Reported', 'State', 'Time'], dtype='object')

# Example 2
ufo.drop(['City', 'State'], axis=1, inplace=True)
columns = ufo.columns
print(columns)

# Output:
# Index(['Shape_Reported', 'Time'], dtype='object')

# Example 3
print(ufo.head())

#Output:
  # Shape_Reported             Time
# 0       TRIANGLE   6/1/1930 22:00
# 1          OTHER  6/30/1930 20:00
# 2           OVAL  2/15/1931 14:00
# 3           DISK   6/1/1931 13:00
# 4          LIGHT  4/18/1933 19:00

ufo.drop([0, 1], axis=0, inplace=True)
print(ufo.head())

# Output:
#   Shape_Reported             Time
# 2           OVAL  2/15/1931 14:00
# 3           DISK   6/1/1931 13:00
# 4          LIGHT  4/18/1933 19:00
# 5           DISK  9/15/1934 15:30
# 6         CIRCLE   6/15/1935 0:00