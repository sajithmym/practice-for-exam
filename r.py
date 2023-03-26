import random

# Generate a random integer between 1 and 10
num = random.randint(1, 10)
print("Random integer:", num)

# Generate a random float between 0 and 1
flt = random.random()
print("Random float:", flt)

# Generate a random boolean value
bool_val = random.choice([True, False])
print("Random boolean:", bool_val)

# Shuffle a list in random order
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Shuffled list:", my_list)
