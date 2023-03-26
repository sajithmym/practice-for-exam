my_list = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, my_list))
print(squares)

my_list = [1, 2, 3, 4]
odds = list(filter(lambda x: x % 2 != 0, my_list))
print(odds)

from functools import reduce

my_list = [1, 2, 3, 4]
product = (reduce(lambda x, y: x * y, my_list))
print(product)

