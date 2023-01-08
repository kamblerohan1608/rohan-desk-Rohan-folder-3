# real calculator with sign and input

def sign ():
    global k

    if c == "+":          #c : decides the operator of the oprtation and perform operation accordingly
        k=a+d
        print(k)          #k : stores the result and is used as first input for next operation
    elif c == "-":
        k=a-d
        print(k)
    elif c == "*":
        k=a*d
        print(k)
    elif c == "/":
        k=a/d
        print(k)
    elif c =="^":
        k=a**d
        print(k)

print("************************ WELCOME TO THE CALCULATOR ****************************")
print()
print("Step 1 : Enter the first number (e.g. :  1)")
print("Step 2 : Enter the operation you want and secound number (e.g. : +1)")
print("Step 3 : If want to do operation on the previous result enter sign and number againg in continuation. (e.g. -1)")
print("NOTE : If want to reset the calculator type c and enter, calculator will be reset.")
print("NOTE : You can perform operations like ( + , - , * , / , ^ )")

s=0         # s : This decides the input should be taken one or two. if s==0 it will take two inputs,
            #    if s==1 it will take only secound input as first input is the result of the previous operation
c=0
def main():
    global s
    if s == 0:
        print()
        global a
        a=float(input("Enter the number : "))               #a : first INT input
        global n
        n=["1","2","3","4","5","6","7","8","9","0","."]
        j=1                                                 #j : to enter the infinite loop
        while j != 0 :
            z=0
            b = input("Enter the action and number : ")      #b : secound input
            if b == "c" or b == "C":
                s=0
                break            
            global c                                         #c : sagrigates sign from the secound input
            c=b[0]
            global op
            op=["+","-","*","/","^"]
            if c not in op:                                  # varifing sign is there before the number or not 
                print("Enter the operation first befor number.")
                z=z+1
            else:                
                global d                                         #d : sagrigate secound number from the secound input(b)
                d=b[1:]            
                for i in d:            # verifies the secound no. sagrigated in d is valid or not
                    if i in n:
                        pass            
                    else:
                        print("invalid input ",i, "inbetween secound number")
                        z=z+1
            if z == 0 :                    #identifies proper inputs and if correct i.e is z == 0,converts d from string to float
                d=float(d)
                sign()
                s = 1
                break
            
    else:
        a = k                          # result of first inputs is assigned as first number for further operations 
        i=1
        while i != 0 :
            n=["1","2","3","4","5","6","7","8","9","0","."]
            z=0
            b = input("Enter the action and number : ")
            if b == "c" or b == "C":
                s=0
                break                            
            c=b[0]
            if c not in op:
                print("Enter the operation first before number. ")
                z=z+1
            else:                                    
                d=b[1:]                
                for i in d:
                    if i in n:
                        pass            
                    else:
                        print("invalid input ",i, "inbetween secound number")
                        z=z+1
            if z == 0 :                    
                d=float(d)
                sign()
                s = 1
                break
                    
while True:

    main()
