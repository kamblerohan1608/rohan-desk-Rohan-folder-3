
# Method Overriding 

# Method overriding is used for accessing the properties of methods having same name but present in different classes

class A:
    def show(self):
        print("Rohan")
class B(A):
    def show(self):
        print("Sumit")
        super().show()        # Step to achieve method overriding

obj = B()
obj.show()
