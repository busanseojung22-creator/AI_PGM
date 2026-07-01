number = int(input("Enter a number to caluculate its factorial: "))
factorial = 1
for i in range(number, 0, -1):
    print(i, end="")
    if i !=1:
        print(" x ", end="")

for i in range(number, 0, -1):
    factorial *= i

print(f" = {factorial}")


