from prettytable import PrettyTable
table=PrettyTable()

list=[]
def signup():
    email=input("enter email id: ")
    password=input("enter password: ")
    if email.endswith("@gmail.com"):
        a={}
        a["email"]=email
        a["password"]=password
        list.append(a)
        print("Registration successful")
        return
    else:
        print("enter valid email id")
        return

    

def signin():
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    x=len(list)
    for i in range(x):
        if email.endswith("gmail.com"):
            if list[i]['email']!=email:
                print("email is not registered, please signUp first.")
                return
            else:
                if(list[i]['password']!=password):
                    print("Incorrect password.")
                    return
                else:
                    print("Login successfull.")
                    return
        else:
            print("entar valid email id")
            

def show():
    table.field_names=["email","password"]
    for i in list:
        table.add_row([i["email"],i["password"]])    
    print(table)




def main():
    while True:
        key=int(input('''\nEnter 0 for signup...
                      \nEnter 1 for signin...
                      \nEnter 2 to exit...
                      \nEnter 3 to show'''))
        if(key==2):
            break
        elif(key==0):
            signup()
        elif(key==1):
            signin()
        elif(key==3):
            show()
        else:
            print("Please enter a valid parameter.")

main()