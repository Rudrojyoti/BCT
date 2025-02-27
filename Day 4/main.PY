import math
# def add(num1,num2): 
#  print("Result:", num1 + num2)

# def sub(num1,num2):
#         print("Result:", num1 - num2)

# def mult(num1,num2):
#     if (num2 or num1)!= 0:
#         print("Result:", num1 * num2)
#     else:
#         print("Result:0")

# def div(num1,num2):
#     if num2 != 0:
#         print("Result:", num1 / num2)
#     else:
#         print("Error: Division by zero")

# def index(num1,num2):
#     print("Result:",pow(num1,num2))
import calc
a = int(input("Enter first number:"))
operator = input("Enter choice:")
b = int(input("Enter second number:"))

if operator == '+':
    calc.add(a,b)
    
elif operator == '-':
    calc.sub(a,b)

elif operator == '*':
    calc.mult(a,b)
    
elif operator == '/':
    calc.div(a,b)

elif operator=='.':
    calc.power(a,b)
    
else:
    print("Invalid choice")
