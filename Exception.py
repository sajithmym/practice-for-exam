# class MyException(Exception):
#     def __init__(self, message):
#         self.message = message

try:
    x = int(input("Enter a number greater than 10: "))
    if x <= 10:
        raise Exception()
except Exception as e:
    print("sfsed")
else:
    print("Number is:", x)
