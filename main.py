from math import sqrt
while True:
    n = int(input("type a number "))
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                print(n," = not a prime number")
                break
        else:
            print(n," = prime number")
    else:
        print(n," = not a prime number")