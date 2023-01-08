#inheritance heirarchichal constructor with parameters

class A:
    def __init__(self,sch_name,sch_location,sch_medium,sch_rank):
        self.sch_name = sch_name
        self.sch_location = sch_location
        self.sch_medium = sch_medium
        self.sch_rank = sch_rank
class B(A):
    def __init__(self,tec_name,tec_subject,tec_salary,tec_age,sch_name,sch_location,sch_medium,sch_rank):
        self.tec_name = tec_name
        self.tec_subject = tec_subject
        self.tec_salary = tec_salary
        self.tec_age = tec_age
        super().__init__(sch_name,sch_location,sch_medium,sch_rank)
class C(A):
    def __init__(self,stu_name,stu_roll,stu_marks,stu_loc,sch_name,sch_location,sch_medium,sch_rank):
        self.stu_name = stu_name
        self.stu_roll = stu_roll
        self.stu_marks = stu_marks
        self.stu_loc = stu_loc
        super().__init__(sch_name,sch_location,sch_medium,sch_rank)
class D(A):
    def __init__(self,std_7,std_8,std_9,std_10,sch_name,sch_location,sch_medium,sch_rank):
        self.std_7 = std_7
        self.std_8 = std_8
        self.std_9 = std_9
        self.std_10 = std_10
        super().__init__(sch_name,sch_location,sch_medium,sch_rank)

obj = D(25000,35000,45000,65000,"swami","Mulund","English",10)
print("The fees for 9th standard students of ",obj.sch_name ,"is",obj.std_9)

obk = C("Sumit",33,651,"Sion","swami","Mulund","English",10)
print()
print(obk.stu_name," is in ",obk.sch_name)

obl = B("Madhuri","Chemistry",35000,40,"swami","Mulund","English",10)
print()
print(obl.tec_name," teaches in ",obj.sch_name)