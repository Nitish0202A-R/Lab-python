def fact(k):
    fact = 1
    for i in range(2, k + 1):
        fact *= i
    return fact

x = int(input("Enter a number: "))
res = fact(x)
print(res)
