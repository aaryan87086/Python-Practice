num = int(input("Enter the number here:"))

if (num %2 ==0 and num>0):
    print("The number is Positive and even")
elif (num%2 ==0 and num<0):
    print("The number is Negative but even")
elif(num % 2 != 0 and num<0 ):
    print("The number is Negative and odd")
elif (num %2 != 0 and num>0):
    print("The number is Positive but odd")
else:
    print("Invalid Number")
