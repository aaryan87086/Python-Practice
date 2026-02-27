# Program to find sum of numbners till n using for loop 
num = int(input("Enter the Number Here :"))
sum = 0

for i in range(1 , num+1):
    sum += 1

print("Sum is " , sum )

# Program to find sum of numbers till n using while loop
num = int(input("Enter the number here :"))
i = 1
total = 0

while i <= num :
    total = total + i
    i +=1

print(" The Sum of number is " , total )