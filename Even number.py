def print_even_numbers(a):
    for i in range(1, a + 1):
        if i % 2 == 0:  # Check if the number is even
            print(i)

x = int(input("Enter a number: "))
print_even_numbers(x)

