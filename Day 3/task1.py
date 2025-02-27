def sum(n):
    if(n==1):
        return 1
    else:
        return n+sum(n-1)
        
a=int(input("enter a number= "))
b=sum(a)
print("the result is=",b)