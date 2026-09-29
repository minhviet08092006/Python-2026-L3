m,n = map(int, input().split())
for i in range(n):
    print("*", end = " ")
print("")
for i in range(m - 2):
    for j in range(n):
        if (j == 0 or j == n -1):
            print("*", end = " ")
        else:
            print(end = "  ")
    print("")
for i in range(n):
    print("*", end = " ")