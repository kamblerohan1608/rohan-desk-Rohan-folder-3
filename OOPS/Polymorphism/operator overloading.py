
# # Operator overloading : 

# print(type(0))
# print(type(10.2))
# print(type('ROHAN'))

# print(10+5)
# print(int.__add__(10,5))

# print(10-5)
# print(int.__sub__(10,5))

# print(10*5)
# print(int.__mul__(10,5))

# class A:
#     def __init__(self,a):
#         self.a = a
#     def __add__(self,other):
#         return self.a + other.a
#     def __sub__(self,other):
#         return self.a - other.a
#     def __mul__(self,other):
#         return self.a * other.a
#     def __lt__(self,other):
#         if self.a < other.a:
#             return (self.a, "is small number")
#         else:
#             return (self.a,"is great number")

# x = A(100)
# y = A(20)
# print(x<y)

# # Changing the operation type od operants :

# class A:
#     def __init__(self,a):
#         self.a = a
#     def __add__(self,other):
#         return self.a - other.a
#     def __sub__(self,other):
#         return self.a + other.a
#     def __mul__(self,other):
#         return self.a / other.a
#     def __lt__(self,other):
#         if self.a > other.a:
#             return (self.a, "is small number")
#         else:
#             return (self.a,"is great number")

# x = A(100)
# y = A(20)
# print(x<y)

class C:
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
        return self.a * other.a
class D:
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
        return self.a / other.a

x = C(5)
y = D(10)

print(x+y)
print(y+x)
