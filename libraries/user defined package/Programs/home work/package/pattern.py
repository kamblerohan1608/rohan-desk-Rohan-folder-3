
# This is the program for patterns.



def right_angle(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()

def inverse_right_angle(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end = " ")
        print()

def mirror_right_angle(n):
    for i in range(n):
        for j in range(n-1-i):
            print(" ",end = " ")
        for k in range(i+1):
            print("*",end=" ")
        print()

def mirror_inverse(n):
    for i in range(n):
        for j in range(i):
            print(" ",end=" ")
        for k in range(n-i):
            print("*",end=" ")
        print()

def right_arrow(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()
    for k in range(n-1):
        for l in range(n-1-k):
            print("*",end=" ")
        print()

def left_arrow(n):
    for i in range(n):
        for j in range(n-1-i):
            print(" ",end=" ")
        for k in range(i+1):
            print("*",end=" ")
        print()
    for l in range(n-1):
        for m in range(l+1):
            print(" ",end=" ")
        for o in range(n-1-l):
            print("*",end=" ")
        print()
def up_arrow(n):
    for i in range(n):
        for j in range(n-1-i):
            print(" ",end=" ") 
        for k in range(i+1):
            print("*",end=" ")
        for l in range(i):
            print("*",end=" ")
        print()

def down_arrow(n):
    for i in range(n):
        for j in range(i):
            print(" ",end=" ")
        for k in range(n-i):
            print("*",end=" ")
        for l in range(n-1-i):
            print("*",end=" ")
        print()


