def f(a):
    original = a
    rev = 0
    while a > 0:
        d = a % 10
        rev = rev * 10 + d
        a = a // 10
    return rev == original

x = int(input("Enter a number: "))
res = f(x)
if res:
    print("palindrome")
else:
    print("not palindrome")