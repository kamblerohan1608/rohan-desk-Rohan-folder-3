#inheritance heirarchical without constructor
'''
class A:
    def school(self):
        self.sch_name = "DBS"
        self.sch_location = "Vashi"
        self.sch_medium = "English"
        self.sch_rank = 2
class B(A):
    def teacher(self):
        self.tec_name = "Madhvi"
        self.tec_subject = "Maths"
        self.tec_salary = 32000
        self.tec_age = 28
class C(A):
    def student(self):
        self.stu_name = "Kiran"
        self.stu_roll = 89
        self.stu_marks = 658
        self.stu_loc = "Parel"
class D(A):
    def fees_structure(self):
        self.std_7 = 12000
        self.std_8 = 15000
        self.std_9 = 20000
        self.std_10 = 35000

obj = D()
obj.fees_structure()
obj.school()
print("The fees for 9th standard students of ",obj.sch_name ,"is",obj.std_9)

obk = C()
obk.student()
obk.school()
print()
print(obk.stu_name," is in ",obk.sch_name)

obl = B()
obl.teacher()
print()
print(obl.tec_name," teaches in ",obj.sch_name)

'''

#inheritance heirarchical constructor without parameter

class A:
    def __init__(self):
        self.sch_name = "DBS"
        self.sch_location = "Vashi"
        self.sch_medium = "English"
        self.sch_rank = 2
class B(A):
    def __init__(self):
        self.tec_name = "Madhvi"
        self.tec_subject = "Maths"
        self.tec_salary = 32000
        self.tec_age = 28
        super().__init__()
class C(A):
    def __init__(self):
        self.stu_name = "Kiran"
        self.stu_roll = 89
        self.stu_marks = 658
        self.stu_loc = "Parel"
        super().__init__()
class D(A):
    def __init__(self):
        self.std_7 = 12000
        self.std_8 = 15000
        self.std_9 = 20000
        self.std_10 = 35000
        super().__init__()

obj = D()
print("The fees for 9th standard students of ",obj.sch_name ,"is",obj.std_9)

obk = C()
print()
print(obk.stu_name," is in ",obk.sch_name)

obl = B()
print()
print(obl.tec_name," teaches in ",obj.sch_name)
