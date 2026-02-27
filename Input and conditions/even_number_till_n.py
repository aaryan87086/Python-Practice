# Program to write even number till n using for loop
num = int(input("Enter the number :"))

for i in range(1, num+1):
    if  i %2 == 0 :
        print(i)


# Program to write even number using While loop
num = int(input("Enter the number :"))

i = 1
while (i <= num):
    if i % 2 == 0 :        
        print(i)
    i += 1

