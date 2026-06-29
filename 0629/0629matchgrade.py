score = int(input("Enter your score: "))
onedigit = score // 10
match onedigit:
    case 10 | 9 :
        print("Excellent!")
    case 8:
        print("Good job!")     
    case 7:
        print("You can do better")     
    case 6:
        print("You need to work harder")     
    case _:
        print("You need to improve your preformance. ")

print("Thank you for using the grade evaluator .")             



