def pallindrome():    
    a=int(input("enter a number="))
    temp=a
    sum=0
    while a>0:
        r=a%10
        sum=sum*10+r
        a=int(a/10)
    if temp==sum:
        print("its a pallindrome number")
    else:
        print("its not a pallindrome number")
pallindrome()