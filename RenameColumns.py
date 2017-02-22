import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')
#print(ufo.head())

# Output:
#     City Colors Reported Shape Reported State             Time
# 0                Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
# 1           Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
# 2               Holyoke             NaN           OVAL    CO  2/15/1931 14:00
# 3               Abilene             NaN           DISK    KS   6/1/1931 13:00
# 4  New York Worlds Fair             NaN          LIGHT    NY  4/18/1933 19:00

#print(ufo.columns)

# Output:
# Index(['City', 'Colors Reported', 'Shape Reported', 'State', 'Time'], dtype='object')

# Example 1
# ufo.rename(columns = {'Colors Reported':'Colors_Reported','Shape Reported':'Shape_Reported'}, inplace=True)
# print(ufo.columns)

# Output:
# Index(['City', 'Colors_Reported', 'Shape_Reported', 'State', 'Time'], dtype='object')

# Example 2
ufo_cols = ['City', 'Colors_Reported', 'Shape_Reported', 'State', 'Time']
# ufo.columns = ufo_cols
# print(ufo.columns)

# Output:
# Index(['City', 'Colors_Reported', 'Shape_Reported', 'State', 'Time'], dtype='object')

# Example 3
# ufo = pd.read_csv('http://bit.ly/uforeports', names=ufo_cols, header=0)
# print(ufo.head())

# Output:
#                    City Colors_Reported Shape_Reported State             Time
# 0                Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
# 1           Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
# 2               Holyoke             NaN           OVAL    CO  2/15/1931 14:00
# 3               Abilene             NaN           DISK    KS   6/1/1931 13:00
# 4  New York Worlds Fair             NaN          LIGHT    NY  4/18/1933 19:00

# Example 4
ufo.columns = ufo.columns.str.replace(' ', '_')
print(ufo.columns)

# Output:
# Index(['City', 'Colors_Reported', 'Shape_Reported', 'State', 'Time'], dtype='object')
