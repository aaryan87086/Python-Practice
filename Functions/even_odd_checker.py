def check(num):
    if num % 2 == 0:
        return "Even"
    else :
        return "Odd"

num = int(input("Enter the number here :"))
result = check(num)
print("The result is" , result)