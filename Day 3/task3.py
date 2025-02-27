
sum=lambda n: 1 if n==1 else n+sum(n-1)
fact=lambda m: 1 if m==1 else m*fact(m-1)

num=int(input("Enter a number"))
print("the sum is=",sum(num))
print("the factorial is=",fact(num))