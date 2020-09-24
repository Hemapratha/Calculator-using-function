def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def divi(a,b):
    return a/b

def operation(choice,a,b):
    while choice >= 0:
        if choice == 1:
            print(add(a, b))
        elif choice == 2:
            print(sub(a, b))
        elif choice == 3:
            print(mul(a, b))
        elif choice == 4:
            print(divi(a, b))
        c=input("Enter the operation is y or n :")
        if c=='y':
            inputfun()
        else:
            break

def inputfunction():
    a = int(input("Enter the 1st numbers"))
    b = int(input("Enter he 2nd number"))
    print("0-- Clear operation")
    print("1 -- Add operation")
    print("2 -- Sub operation")
    print("3 -- Mul operation")
    print("4 -- Division operation")
    choice = int(input("Enter the choice: "))
    operation(choice,a,b)

inputfunction()
