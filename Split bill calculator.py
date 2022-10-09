# Exercise 1

# bill = eval(input("Enter amount of bill: "))
# people = eval(input("Enter number of people: "))
# tipsAmount = float(input("Enter amount of tips (%): "))



# tipsTotal = (bill / people) * (tipsAmount / 100)
# totalAmount = tipsTotal + bill

# print("\nTip amount per person $",'{:.2f}'.format(tipsTotal))
# print("Total amount per person $",'{:.2f}'.format(totalAmount))

# Exercise 2

numberInput = eval(input("Enter a number: "))
if numberInput > 1:
    for i in range(2, numberInput - 1):
        if numberInput % i == 0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")
else:
    print("It is not a prime number")

# Exercise 3

# seconds = eval(input("Enter the number of seconds: "))

# hours = seconds // 3600
# minutes = (seconds % 3600) // 60
# remainSecond = seconds % 60

# print(f"{hours}:{minutes}:{remainSecond}")

