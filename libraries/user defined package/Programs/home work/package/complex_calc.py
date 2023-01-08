
#  This is complex calculator

def factorial(n):
    fact = 1
    for i in range(n,0,-1):
        fact *= i
    return fact

def per(obtain,total):
    if obtain > total :
        obtain,total = total,obtain
    return (obtain*100)/total

def bmi(height,weight):
    return weight/(height/100)**2
