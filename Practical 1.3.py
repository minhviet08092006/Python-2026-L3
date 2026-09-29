n = int(input("Enter a number? "))
if n % 1 == 0 and n % n == 0:
    print(n, "is a prime number.")
else:
    print(n, "is a NOT prime number.")