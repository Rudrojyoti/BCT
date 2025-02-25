list=[]
def signup():
    email=input("enter email id: ")
    password=input("enter password: ")
    a={}
    a["email= "]=email
    a["password= "]=password
    list.append(a)
    print("Registration successful")
    return

def signin():
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    x=len(list)
    for i in range(x):
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


def main():
    while True:
        key=int(input('''\nEnter 0 for signup...
                      \nEnter 1 for signin...
                      \nEnter 2 to exit...'''))
        if(key==2):
            break
        elif(key==0):
            signup()
        elif(key==1):
            signin()
        else:
            print("Please enter a valid parameter.")

main()

