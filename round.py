# Rounding a float to 2 decimal places
x = 3.14159
y = round(x, 2)
print(y)  # Output: 3.14

# Rounding an integer to the nearest 10
x = 37
y = round(x, -1)
print(y)  # Output: 40

# Rounding a float to the nearest integer
x = 4.6
y = round(x)
print(y)  # Output: 5

x = 'v'
print(type(id(x)))  # Output: <class 'int'>

mango = "fruit"
apple = mango
print(apple)  # Output: "fruit"


t = (1,2,4,3)
print(t[1:3])

t = [1,2,4,3,8,9]
print(t[i] for i in range(0,len(t),2))

my_set = {1, 2, 3}
my_set.add(4)
my_set.update([5, 6, 7])
print(my_set)