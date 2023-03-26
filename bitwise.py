a = 0b1100  # binary representation of 12
b = 0b1010  # binary representation of 10
c = a & b   # bitwise AND of a and b
print(bin(c))   # Output: 0b1000 (binary representation of 8)
print()

a = 0b1100  # binary representation of 12
b = 0b1010  # binary representation of 10
c = a | b   # bitwise OR of a and b
print(bin(c))   # Output: 0b1110 (binary representation of 14)
print()

a = 0b1100  # binary representation of 12
b = 0b1010  # binary representation of 10
c = a ^ b   # bitwise XOR of a and b
print(bin(c))   # Output: 0b0110 (binary representation of 6)
print()

a = 0b1100  # binary representation of 12
b = ~a      # bitwise NOT of a
print(bin(b))   # Output: -0b1101 (binary representation of -13)
print()

a = 0b1100  # binary representation of 12
b = a << 2  # left shift a by 2 positions
print(bin(b))   # Output: 0b110000 (binary representation of 48)
print()

a = 0b1100  # binary representation of 12
b = a >> 2  # right shift a by 2 positions
print(bin(b))   # Output: 0b0011 (binary representation of 3)
print()

def divide(a, b):
    assert b != 0, "division by zero Error"
    return a / b

print(divide(10, 2))  # Output: 5.0

try:
    print(divide(10, 0))  # Output: AssertionError: division by zero
except Exception as e:
    print(e)

code = '''
for i in range(5):
    print(i)
'''

exec(code)
print()

def my_range(start, stop, step=1):
    i = start
    while i < stop:
        yield i
        i += step

for i in my_range(0, 10, 2):
    print(i)
