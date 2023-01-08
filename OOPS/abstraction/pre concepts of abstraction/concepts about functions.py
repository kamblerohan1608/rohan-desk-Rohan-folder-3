
# # A function can be declared inside another function.(Inner function)
# # A function can be used as return of another function.
# # A function can be used as parameter to another function.  

# Example 1.

# def A():
#     def B():                        # inner function
#         return "Inner function"
#     return B                        # function as return
# a=A()
# print(a())

# Example 2.

# def king():
#     def queen():
#         a=10
#         b=10
#         return(a+b)
#     return queen

# a=king()
# print(a())

# Example 3.

# Function as a parameter.


# def a():
#     x=10
#     y=20
#     return x+y
# def b():
#     c=20
#     d=30
#     return d-c

# def main(func1,func2):
#     A=func1()
#     B=func2()
#     print(A)
#     print(B)
#     print(A+B)

# main(a,b)

# function as parameter (along with parameters)

def a(x,y):
    return x+y
def b(c,d):
    return d-c

def main(func1,func2,x,y,c,d):
    A=func1(x,y)
    B=func2(c,d)
    print(A)
    print(B)
    print(A+B)

main(a,b,10,15,10,70)
