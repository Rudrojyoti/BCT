
def add(num1,num2): 
 print("Result:", num1 + num2)

def sub(num1,num2):
        print("Result:", num1 - num2)

def mult(num1,num2):
    if (num2 or num1)!= 0:
        print("Result:", num1 * num2)
    else:
        print("Result:0")

def div(num1,num2):
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")

def power(num1,num2):
    print("Result:",pow(num1,num2))