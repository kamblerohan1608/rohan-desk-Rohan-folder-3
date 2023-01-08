
# user defined module

class calculator:
    '''
    This is a calculator module which gives basic maths operations done like 
    addition,substraction,multiplication,division,factorial,and percentages

    it involved

    add(a,b) : requirs two arguments which will return a+b
    sub(a,b) : requirs two arguments which will return a-b
    mul(a,b) : requirs two arguments which will return a*b
    div(a,b) : requirs two arguments which will return a/b
    fact(a) : requirs two arguments which will return a!
    per(obtain,total) : requirs two arguments which will return percentages

    '''
    def add(self,a,b):
        self.a = a
        self.b = b
        '''
        arguments a and b required wich will be giving the addition operation i.e a+b in return
        '''
        return a+b

    def sub(self,a,b):
        self.a = a
        self.b = b
        '''
        arguments a and b required wich will be giving the substraction operation i.e a-b in return
        '''
        return a-b

    def mul(self,a,b):
        self.a = a
        self.b = b
        '''
        arguments a and b required wich will be giving the multiplication operation i.e a*b in return
        '''
        return a*b

    def div(self,a,b):
        self.a = a
        self.b = b
        '''
        arguments a and b required wich will be giving the division operation i.e a/b in return
        it will not be effected if the numbers are miss aranged it will still give the appropriate answer.

        '''
        if b > a:
            a,b = b,a
        return a/b

    def fact(self,a):
        self.a = a
        '''
        argument a required wich will be giving the factorial operation i.e a! in return
        a!=a*(a-1)*(a-2)*(a-3)......*1

        '''
        fact = 1
        for i in range (a,0,-1):
            fact = fact * i
        return fact
    
    def per(self,obtain,total):
        self.obtain = obtain
        self.total = total
        '''
        arguments for obtained marks(obtain) and for total marks(total) is required 
        wich will return percentages.
        the sequence of this arguments will nit matter even if miss aranged it will provide proper value.

        '''
        if obtain>total:
            obtain,total = total,obtain

        return (obtain*100)/total

