num1=int(input("Enter First Number :"))
num2=int(input("Enter Second Number :"))
num3=int(input("Enter Third Number :"))

if (num1>=num2 and num1>=num3):
    print("The Largest Number is ",num1)

elif(num3>=num2 and num3>=num1):
    print("The Largest Number is ",num3)
else:
    print("The Largest Number is ",num2)