number = int(input("Enter a number: "))

for i in range(1, number + 1):

    # 공백 출력
    for j in range(number - i):
        print(" ", end="")

    # 별 출력
    for j in range(i):
        print("*", end="")

    print()