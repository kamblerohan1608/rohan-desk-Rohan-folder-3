
# Duck Typing :

# # If it feels like duck,works like duck and sounds like duck then it is a duck.

# # Python does not care from which class or object it is getting the property, if it is getting the property thats it.

# # Example :

# class India:
#     def capital(self):
#         print("The capital of India is Delhi.")
#     def language(self):
#         print("The langauge spoken is Hindi.")

# class USA:
#     def capital(self):
#         print("The capital of USA is Washington DC.")
#     def language(self):
#         print("The langauge spoken is English.")
        
# A = India()
# B = USA()        
# for i in (A,B):
#     i.capital()
#     i.language()
    
# Example 2 :

class A:
    def add(self):
        self.a = 10
        self.b = 10
        print(self.a+self.b)
class B:
    def add(self):
        self.a = 10
        self.b = 10
        print(self.a*self.b)

c=A()
d=B()
def main(obj):
    obj.add()

main(c)
main(d)