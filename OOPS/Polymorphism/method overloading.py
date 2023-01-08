
# # Method Overloading : 

# # 1. Various tasks by single method :

# #Python does not support method overloading directly but it can be achieved by multidispatch library

# from multipledispatch import dispatch

# class A:
#     @dispatch()
#     def add(self):
#         return (20+30)
#     @dispatch(int)
#     def add(self,a):
#         return (a - 30)
#     @dispatch(int,int)
#     def add(self,a,b):
#         return (a*b)

# c = A()
# print(c.add())
# print(c.add(20))
# print(c.add(20,30))

# # 2.Using length function which can be used to find length of various data either in string, list or tupple

# class B:
#     def length(self,data):
#         return (len(data))

# obj = B()

# a='Rohan Hanumant Kamble'
# b=[1,2,3,4,5,6,7,8,9]
# c=(1,2,3,4,5)

# print(obj.length(a))
# print(obj.length(b))
# print(obj.length(c))

# # 3. adding data of different no. of parameters passed by *args : 

# from re import S


# class C:
#     def sum (self,*args):
#         s=0
#         for i in args:
#             s=s+i
        
#         return s

# D=C()
# print(D.sum(0,1,2,3,4,5))
# print(D.sum(5,6,7,8,9,10))