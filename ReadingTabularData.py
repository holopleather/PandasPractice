import pandas as pd

#Example 1
orders = pd.read_table('http://bit.ly/chiporders')
#print(orders.head())

#Output:

 # order_id  quantity                              item_name  \
# 0         1         1           Chips and Fresh Tomato Salsa
# 1         1         1                                   Izze
# 2         1         1                       Nantucket Nectar
# 3         1         1  Chips and Tomatillo-Green Chili Salsa
# 4         2         2                           Chicken Bowl
#
#                                   choice_description item_price
# 0                                                NaN     $2.39
# 1                                       [Clementine]     $3.39
# 2                                            [Apple]     $3.39
# 3                                                NaN     $2.39
# 4  [Tomatillo-Red Chili Salsa (Hot), [Black Beans...    $16.98

#Example 2
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
user = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols)
#print(user.head())

#Output:

   # user_id  age gender  occupation zip_code
# 0        1   24      M  technician    85711
# 1        2   53      F       other    94043
# 2        3   23      M      writer    32067
# 3        4   24      M  technician    43537
# 4        5   33      F       other    15213