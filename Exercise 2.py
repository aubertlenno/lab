# lowerBound = int(input("Enter lower bound: "))
# upperBound = int(input("Enter upper bound: "))

# numbers = range(lowerBound,upperBound+1)
# even = []
# odd = []

# while lowerBound < 0:
#     lowerBound = int(input("Enter a positive number: "))
# else:
#     for i in numbers:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)

# print(odd)
# print(even)


pyramid = int(input("Enter height of pyramid: "))

height = range(1,pyramid + 1)

for i in height:
    print(str(i) * i)