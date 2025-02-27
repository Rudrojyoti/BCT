
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
        
a=int(input("enter a number= "))
b=fact(a)
print("the result is=",b)