
# Calculator

from math_module import calculator

print("***************** Welcome to calculator *********************")
print()
print("Choose option from below :")
print("Press 1 - Addition")
print("Press 2 - Substraction")
print("Press 3 - Multiplication")
print("Press 4 - Division")
print("Press 5 - Percentage")
print("Press 6 - Factorial")
print("Press 7 - Exit")

calc = calculator()
while True : 
    print()
    ch = int(input("Enter your choice : "))

    if (ch == 1):
        a = int(input("Enter the first number for addition : "))
        b = int(input("Enter the secound number for addition : "))
        print("The addition is : ",calc.add(a,b))
    elif (ch == 2):
        a = int(input("Enter the first number for substraction: "))
        b = int(input("Enter the secound number for substraction: "))
        print("The substraction is : ",calc.sub(a,b))
    elif (ch == 3):
        a = int(input("Enter the first number for multiplication : "))
        b = int(input("Enter the secound number for multiplication : "))
        print("The multiplication is : ",calc.mul(a,b))
    elif (ch == 4):
        a = int(input("Enter the first number division : "))
        b = int(input("Enter the secound number division : "))
        print("The division is : ",calc.div(a,b))
    elif (ch == 5):
        a = int(input("Enter the marks obtained : "))
        b = int(input("Enter the total marks : "))
        print("The percentages are : ",calc.per(a,b))
    elif (ch == 6):
        a = int(input("Enter the number for factorial : "))
        print("The factorial is : ", calc.fact(a))
    elif (ch == 7):
        print()
        print("************** You have exited the program********************")
        print()
        print("**********************Thank You***************************")
        print()
        break
    else:
        print("Invalid choice.\n Enter the appropriate choice.")
