n = int(input("Enter a number? "))
sum = 0 
for i in range(1, int(n/2) + 1):
    n % i == 0
    sum += i
if sum == n:
    print(n, "is a perfect number.")
else:
    print(n, "is a Not perfect number.")
