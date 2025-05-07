def countdown(k):
    if k < 0:
        return  # Stop recursion if k is negative
    print(k)
    countdown(k - 1)  # Recursive call

x = int(input("Enter a number: "))
countdown(x)
