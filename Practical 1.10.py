n = int(input("Enter a number: "))
def divisors(n):
    divisors_list = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors_list.append(i)
    return divisors_list
print(divisors(n))
        
        