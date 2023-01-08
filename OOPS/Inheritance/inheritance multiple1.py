# inheritance multiple without constructor
'''
class A:
    def bus(self):
        self.bus_name = "BEST"
        self.bus_seats = 50

class B:
    def train(self):
        self.train_name = "Express"
        self.train_seats = 1000
class C(A,B):
    def plane(self):
        self.plane_name = "Emirits"
        self.plane_seats = 700

obj = C()
obj.bus()
obj.train()
obj.plane()
print("Plane information")
print("Name of the plane is : ",obj.plane_name)
print("Seats in the plane are : ",obj.plane_seats)
print()
print("Train information")
print("Name of the train is : ",obj.train_name)
print("Seats in the train are : ",obj.train_seats)
print()
print("Bus information")
print("Name of the bus is : ",obj.bus_name)
print("Seats in the bus are : ",obj.bus_seats)
'''

#inheritance multiple constructor without parameters

class student:
    def __init__(self):
        self.stu_name = "Kiran"
        self.stu_roll = 89
        self.stu_marks = 658
        self.stu_loc = "Parel"
        
class teacher:
    def __init__(self):
        self.tec_name = "Madhvi"
        self.tec_subject = "Maths"
        self.tec_salary = 32000
        self.tec_age = 28
        
        
class school(student,teacher):
    def __init__(self):
        
        self.sch_name = "Swami"
        self.sch_loc = "Andheri"
        self.sch_fees = 95000
        self.sch_rank = 3
        super().__init__()
        teacher.__init__(self)

obj = school()
print("School name is : ",obj.sch_name)
print("School fees are : ", obj.sch_fees)
print("Student name is : ",obj.stu_name)
print("Student location  is : ",obj.stu_loc)
print("Teacher name is : ",obj.tec_name)
print("Teacher's subject is : ",obj.tec_subject)
