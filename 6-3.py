import pandas as pd

data = {
	'apples': [4, 2, 6, 5],
	'bananas': [1, 3, 2, 6]
}

index = ['Aaron', 'Lee', 'Steve', 'Shaun']
purchases = pd.DataFrame(data, index=index)
print(purchases)

"""
Output
			 apples  bananas
Aaron       4        1
Lee         2        3
Steve       6        2
Shaun       5        6
"""
print(purchases.loc['Lee'])

"""
Output
apples     2
bananas    3
Name: Lee, dtype: int64
"""