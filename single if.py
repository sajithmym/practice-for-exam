x = 5
y = "greater than 5" if x > 5 else "less than or equal to 5"
print(y)  # Output: "less than or equal to 5"

print("welcome") if x>10 else print("do some change")

print(round(8553.14586,-3))

# syntax error 
# name error 
# type error 
# value error 
# index error 

my_set = {1, 2, 3, 4, 5}
# my_set.remove(1)
my_set.discard(5)
print(my_set)


print('\n \n')

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
symmetric_difference = set1 ^ set2
print(symmetric_difference)  # Output: {1, 2, 5, 6}

print('\n \n')

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)  # Output: {1, 2, 5, 6}

[print(i**2) for i in range(1,11)]
print('hi, hellow') if False else print('okay')