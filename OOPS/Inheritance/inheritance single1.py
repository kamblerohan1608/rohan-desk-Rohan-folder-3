'''
# Single inheritance

#Example 1

class A:
    def stu_info(self):
        self.stu_name = "Rohan"
        self.stu_age = 14
        self.stu_loc = "Kurla"
        self.stu_contact = 54698745632
        self.stu_roll_no = 12
        self.stu_class = 8

    def course_info(self):
        self.course_name = "MS-CIT"

class B(A):
    def emp_info(self):
        self.emp_name = "Sameer"
        self.emp_age = 24
        self.emp_loc = "Bandra"
        self.emp_contact = 4896231565
        self.emp_id = 456

    def certification(self):
        self.certificates = "Automation Anywhere"

obj=B()
obj.emp_info()
obj.stu_info()
obj.course_info()
obj.certification()
print("Employee name is : ",obj.emp_name)
print("Employee id is : ",obj.emp_id)
print("Employee certifications are : ",obj.certificates)
print("Student name is : ",obj.stu_name)
print("Student roll no. is : ",obj.stu_roll_no)
print("Student course : ", obj.course_name)

# Example 2

class A:
    def __init__(self):
        self.stu_name = "Rohan"
        self.stu_age = 14
        self.stu_loc = "Kurla"
        self.stu_contact = 54698745632
        self.stu_roll_no = 12
        self.stu_class = 8

    def course_info(self):
        self.course_name = "MS-CIT"

class B(A):
    def __init__(self):
        self.emp_name = "Sameer"
        self.emp_age = 24
        self.emp_loc = "Bandra"
        self.emp_contact = 4896231565
        self.emp_id = 456
        super().__init__()

    def certification(self):
        self.certificates = "Automation Anywhere"

obj=B()

print("Employee name is : ",obj.emp_name)
print("Employee id is : ",obj.emp_id)

print("Student name is : ",obj.stu_name)
print("Student roll no. is : ",obj.stu_roll_no)

obj.course_info()
obj.certification()
print("Employee certifications are : ",obj.certificates)
print("Student course : ", obj.course_name)

'''
# Exapmle 3

class A:
    def __init__(self):
        self.stu_name = "Rohan"
        self.stu_age = 14
        self.stu_loc = "Kurla"
        self.stu_contact = 54698745632
        self.stu_roll_no = 12
        self.stu_class = 8

    def course_info(self):
        self.course_name = "MS-CIT"

class B(A):
    def __init__(self):
        self.emp_name = "Sameer"
        self.emp_age = 24
        self.emp_loc = "Bandra"
        self.emp_contact = 4896231565
        self.emp_id = 456
        super().__init__()

    def certification(self):
        self.certificates = "Automation Anywhere"

obj=B()
def main():
    print("*****************************************************************************************************")
    print()
    print("************************ Enter your choice for Student/Employ information ***************************")
    print()
    print("Press 1 - Student information")
    print("Press 2 - Employ information")
    print("Prrss 0 - To Exit")
    print()

main()
s = 0
while True:
    if s >= 1:
        main()
    print()
    ch=int(input("Enter your choice of Student/Employ information : "))
    print()

    if ch==1: 
        def student():

            print()
            print("Press 1 - for student's name")
            print("Press 2 - for student's age")
            print("Press 3 - for student's location")
            print("Press 4 - for student's contact")
            print("Press 5 - for student's roll no")
            print("Press 6 - for student's class")
            print("Press 7 - for all information")
            print("press 0 - To Exit")
            print()
            global s
            s += 1

        student()
        while True:
            print()
            sh=int(input("Enter your choice of student info : "))
            print()
            if sh==1:
                print("Student name is : ",obj.stu_name)
                print()
                student()
            elif sh==2:
                print("Student age is : ",obj.stu_age)
                print()
                student()
            elif sh==3:
                print("Student location is : ",obj.stu_loc)
                print()
                student()
            elif sh==4:
                print("Student contact is : ",obj.stu_contact)
                print()
                student()
            elif sh==5:
                print("Student roll no is : ",obj.stu_roll_no)
                print()
                student()
            elif sh==6:
                print("Student class is : ",obj.stu_class)
                print()
                student()
            elif sh==7:
                print("Student name is : ",obj.stu_name)
                print("Student age is : ",obj.stu_age)
                print("Student location is : ",obj.stu_loc)
                print("Student contact is : ",obj.stu_contact)
                print("Student roll no is : ",obj.stu_roll_no)
                print("Student class is : ",obj.stu_class)
                print()
                student()
            elif sh==0:
                break
            else:
                print("******************************* invalid input ****************************")
                print()
                student()
        
    elif ch==2:
        def employee():

            print()
            print("Press 1 - for Employee's name")
            print("Press 2 - for Employee's age")
            print("Press 3 - for Employee's location")
            print("Press 4 - for Employee's contact")
            print("Press 5 - for Employee's ID")
            print("Press 6 - for all information")
            print("press 0 - To Exit")
            print()
            global s
            s += 1

        employee()

        while True:
            print()
            eh=int(input("Enter your choice of employ info : "))
            print()
            if eh==1:
                print("Employee name is : ", obj.emp_name)
                print()
                employee()
            elif eh==2:
                print("Employee age is : ", obj.emp_age)
                print()
                employee()
            elif eh==3:
                print("Employee location is : ", obj.emp_loc)
                print()
                employee()
            elif eh==4:
                print("Employee contact is : ", obj.emp_contact)
                print()
                employee()
            elif eh==5:
                print("Employee ID is : ", obj.emp_id)
                print()
                employee()
            
            elif eh==6:
                print()
                print("Employee name is : ", obj.emp_name)
                print("Employee age is : ", obj.emp_age)
                print("Employee location is : ", obj.emp_loc)
                print("Employee contact is : ", obj.emp_contact)
                print("Employee ID is : ", obj.emp_id)
                print()
                employee()
            elif eh==0:
                break
            else:
                print()
                print("******************************* invalid input ****************************")
                print()
                employee()
        
    elif ch==0:
        print()
        print("************************ Thank You ******************************")
        print()
        print("******************* You Have Exited The Program **********************")
        print()
        break
    else:
        print()
        print("************************invalid input**************************")
        print()
        s += 1

