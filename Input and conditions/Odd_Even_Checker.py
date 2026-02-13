num = int(input("Enter the number here:"))
if num == 0 :
    print("The number is zero and even")
elif (num>0):
    if(num%2 == 0):
        print("The number is Even and Positive")
    else:
        print("The number is Odd and Positive")

else:
    if(num % 2==0):
        print("The number is Negative and Even")
    else:
        print("The number is Negative and odd")

    