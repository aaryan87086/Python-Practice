n = int(input("Enter the number: "))

if n <= 1:
    print("The number is not prime")
else:
    is_prime = True   # pehle assume kar liya prime hai
    
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("The number is prime")
    else:
        print("The number is not prime")