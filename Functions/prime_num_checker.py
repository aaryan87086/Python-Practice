# Program to Check Number Prime or not
def check(num):
    if (num <= 1):
        return "False"
    
    for i in range(2,num):
        if num % i == 0:
            return(False)
        
    return True

num = int(input("Enter the number :"))

if check(num):
    print("Prime Number")
else :
    print("Not a Prime Number")
        