def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다."
    return a / b


while True:
    print("\n====== 계산기 ======")
    print("1. 덧셈")
    print("2. 뺄셈")
    print("3. 곱셈")
    print("4. 나눗셈")
    print("0. 종료")

    menu = input("메뉴를 선택하세요 : ")

    if menu == "0":
        print("계산기를 종료합니다.")
        break

    if menu not in ["1", "2", "3", "4"]:
        print("잘못된 메뉴입니다.")
        continue

    num1 = float(input("첫 번째 숫자 : "))
    num2 = float(input("두 번째 숫자 : "))

    if menu == "1":
        print(f"결과 : {add(num1, num2)}")

    elif menu == "2":
        print(f"결과 : {sub(num1, num2)}")

    elif menu == "3":
        print(f"결과 : {mul(num1, num2)}")

    elif menu == "4":
        print(f"결과 : {div(num1, num2)}")