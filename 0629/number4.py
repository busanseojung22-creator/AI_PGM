number = int(input("Enter a number: "))

# 위쪽
for i in range(1, number + 1):

    for j in range(number - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()

# 아래쪽
for i in range(number - 1, 0, -1):

    for j in range(number - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()
                