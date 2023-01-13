import pandas as pd

data = {
	'apples': [4, 2, 6, 5],
	'bananas': [1, 3, 2, 6]
}

purchases = pd.DataFrame(data)
print(purchases)

"""
Output
	 apples  bananas
0       4        1
1       2        3
2       6        2
3       5        6
"""