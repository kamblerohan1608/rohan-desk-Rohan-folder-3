
# Usage of user defined package in a program.

from package import simple_calc , complex_calc , pattern


def main_menu():

    print()
    print()
    print("************************ WELCOME TO MY APPLICATION *************************")
    print()
    print()
    print("********************** Choose From The Below Options ***********************")
    print()
    print()
    print("Press 1    -   Simple Calculator")
    print("Press 2    -   Comlex Calculator")
    print("Press 3    -   Pattern ")
    print("Press 4    -   Exit ")
    print()
    print("*****************************************************************************")
    print()
    print()

main_menu()

while True:

    ch = int(input("Enter your choice : "))
    print()
    
    if ch == 1:
        print()
        print("*************************** Simple Calculator ********************************")
        print()
        print("********************** Choose From The Below Options ***********************")
        print()
        print("Press 1    -   Addition")
        print("Press 2    -   Substraction")
        print("Press 3    -   Multiplication")
        print("Press 4    -   Division")
        print("Press 5    -   Power")
        print("Press 6    -   Exit")
        print()

        while True:
            print()
            ch = int(input("Enter the Choice : "))
            print()

            if ch ==1:

                a = int(input("Enter the first number for addition : "))
                b = int(input("Enter the second number for addition : "))
                print("The addition is : ",simple_calc.add(a,b))

            elif ch==2:

                a = int(input("Enter the first number for Substraction : "))
                b = int(input("Enter the second number for Substraction : "))
                print("The substraction is : ",simple_calc.sub(a,b))
            
            elif ch ==3:

                a = int(input("Enter the first number for Multiplication : "))
                b = int(input("Enter the second number for Multiplication : "))
                print("The Multiplication is : ",simple_calc.mul(a,b))
            
            elif ch ==4:

                a = int(input("Enter the first number for Division : "))
                b = int(input("Enter the second number for Division : "))
                print("The Division is : ",simple_calc.div(a,b))
            
            elif ch == 5:

                a = int(input("Enter the first number : "))
                b = int(input("Enter the power for first number : "))
                print("The addition is : ",simple_calc.pow(a,b))
            elif ch == 6:
                print()
                print("***************************** You have Exited *********************************")
                print()
                print("******************* Thank you for using Simple Calculator *********************")
                print()
                main_menu()
                break
            else :
                print()
                print("***************** Invalid Choice Entered. Enter valid choice ******************")
                print()
    elif ch == 2:
        print()
        print("*************************** Complex Calculator********************************")
        print()
        print("********************** Choose From The Below Options ***********************")
        print()
        print("Press 1    -   Factorial")
        print("Press 2    -   Percentage")
        print("Press 3    -   Body Mass Index")
        print("Press 4    -   Exit")
        print()

        while True:
            print()
            ch = int(input("Enter The Choice : "))
            print()

            if ch == 1:

                a = int(input("Enter the number for Factorial : "))
                print()
                print("The Factorial is : ",complex_calc.factorial(a))
                
            elif ch == 2:

                a = int(input("Enter the obtained marks : "))
                b = int(input("Enter the total marks : "))
                print("The percentages are : ",complex_calc.per(a,b),"%")
                
            elif ch == 3:

                a = int(input("Enter the Height in cm : "))
                b = int(input("Enter the weight in Kg : "))
                result = complex_calc.bmi(a,b)
                print("The Body mass index is : ",result)
                print()
                
                if result < 18.5 :
                    print("Result of BMI : Underweight")
                elif result > 18.5 and result < 25 :
                    print("Result of BMI : Normal")
                else:
                    print("Result of BMI : Overweight")

            elif ch == 4:
                print()
                print("***************************** You have Exited *********************************")
                print()
                print("******************* Thank you for using Complex Calculator *********************")
                print()
                main_menu()
                break
            else :
                print()
                print("***************** Invalid Choice Entered. Enter valid choice ******************")
                print()

    elif ch ==3:
        print()
        print("*************************** Pattern Printer ********************************")
        print()
        print("********************** Choose From The Below Options ***********************")
        print()
        print("Press 1    -   Right Angle Triangle")
        print("Press 2    -   Mirror Right Angle Triangle")
        print("Press 3    -   Inverse Right Angle Triangle")
        print("Press 4    -   Inverse Mirror Right Angle Triangle")
        print("Press 5    -   Right arrow")
        print("Press 6    -   Left arrow")
        print("Press 7    -   Up arrow")
        print("Press 8    -   Down arrow")
        print("Press 9    -   Exit")
        print()

        while True:

            print()
            ch = int(input("Enter The Choice : "))
            print()

            if ch == 1:

                a = int(input("Enter the number of rows for pattern : "))
                print()
                pattern.right_angle(a)
                    
            elif ch == 2:

                a = int(input("Enter the number of rows for pattern : "))
                print()
                pattern.mirror_right_angle(a)
                    
            elif ch == 3:

                a = int(input("Enter the number of rows for pattern : "))
                print()
                pattern.inverse_right_angle(a)

            elif ch == 4:

                a = int(input("Enter the number of rows for pattern : "))
                print()
                pattern.mirror_inverse(a)

            elif ch == 5:

                a = int(input("Enter the number of rows for pattern : "))
                print()
                pattern.right_arrow(a)

            elif ch == 6:

                a = int(input("Enter the number of rows for pattern : "))
                print()
                pattern.left_arrow(a)

            elif ch == 7:

                a = int(input("Enter the number of rows for pattern : "))
                print()
                pattern.up_arrow(a)

            elif ch == 8:

                a = int(input("Enter the number of rows for pattern : "))
                print()
                pattern.down_arrow(a)

            elif ch == 9:
                print()
                print("***************************** You have Exited *********************************")
                print()
                print("******************* Thank you for using Pattern Printer ***********************")
                print()
                main_menu()
                break
            else :
                print()
                print("***************** Invalid Choice Entered. Enter valid choice ******************")
                print()
                

    elif ch == 4:
        print()
        print("******************* Thank You For Using The Application ***********************")
        print()
        print()
        print("****************************** HAPPY TO HELP **********************************")
        print()
        print()
        break
    else:
        print()
        print("***************** Invalid Choice Entered. Enter valid choice ******************")
        print()
        print()

