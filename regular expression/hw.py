
import re



# Q .write a program to find a sqquence of lower case letters joint with an underscore

#test = "Hello_world , hi_there , Is_this_ok , thats_me , catch_me"

# def lowercase_function(text):
#     ptr = r'\b[a-z]+_[a-z]+\b'
#     x = re.findall(ptr,text)
#     return x

# text = input("Enter the test line here : ")
# print(lowercase_function(text))



# Q .write a program that matches a string that has an 'a' followed by anything and ends with 'b'

# test = "aaaaaaaaaaa here is the string bbbbbbbbbbb"

# def a_b(text):
#     prt = r'\Aa[a-zA-Z0-9 *]+b\Z'
#     x = re.findall(prt,text)
#     return x

# text = input("Enter the test line here : ")
# print(a_b(text))



# Q .write a python program that matches a word wich contains z

# test = " Crazy syncronization camel puzzle signes "

# def z_word(text):    
#     ptr = r'[a-zA-z]+z+[a-zA-z]+'
#     x = re.findall(ptr,text)
#     return x
# text = input("Enter the test line here : ")
# print(z_word(text))



# Q. identify the smallest pallendrom in the string.

s = '11221122322'
# s='grhfhdfhtd'
print(s)

if s.isdigit()==False:
    print('str provided is not valid.')

else:
    ls=[]
    for i in range(len(s)):
        # print(i)
        n=3
        for j in range(3+i,len(s)):
            # if j <= len(s)-3 :
                # print('value of j is ',j)
                pall=s[i:j]
                # print('pallendrom is :',pall)
                inv_pall=''
                for k in range(len(pall)-1,-1,-1):
                    inv_pall = inv_pall + pall[k]
                # print('inverse of pall :', inv_pall)
                # print(pall,inv_pall)
                if int(pall)==int(inv_pall):
                    ls.append(pall)
    # print(ls)
    ls.sort(reverse=True)
    final_pal_list =[]
    for i in ls:
        if len(i) == len(ls[0]):
            final_pal_list.append(i)
    final_pal_list = ','.join(final_pal_list)
    print('The minimum pallendrom present in the input :',final_pal_list)
