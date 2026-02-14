def largest(a,b,c):
    if (a > b and a > c):
        return a
    elif(b > c and b > a):
        return b
    else:
        return c

num1 = 5
num2 = 7
num3 = 9

Result = largest(num1,num2,num3)
print("Largest Number is " ,Result) 