# a = 5
# b = 10


# print(f"The value of a is {a} and the value of b is {b}.")

# x = 1
# y = 2

# print(f"x = {y}")
# print(f"y = {x}")

# x = 10
# y = 10

# print (x == y)

# i = int(input("Enter a value for i: "))
# print(f"The value of i is {i}")
# print(type(i))

# if x == 5:
#     print("x is more than or equal to 5")
# elif x == 5:
#     print("x is more than or equal to 10")
# else:
#     print("x is less than 5")

# if x > 3:
#     if x > 4:
#         print("x is more than 3 and 4")
#     else:
#         print("x is more than 3 but not 4")
# else:
#     print("x is not more than 3")


length1 = int(input("input length 1: "))
length2 = int(input("input length 2: "))
length3 = int(input("input length 3: "))

perimeter = length1 + length2 + length3

if length1 + length2 > length3:
    print(perimeter)
elif length1 + length3 > length2:
    print(perimeter)
elif length2 + length3 > length1:
    print(perimeter)
else:
    print("Input invalid and cannot be calculated")