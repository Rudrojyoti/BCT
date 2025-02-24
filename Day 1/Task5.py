a=int(input("enter a year= "))
if a%4==0 and (a%400==0 or a%100!=0):
    print("its a leap year")
else:
    print("its not a leap year")