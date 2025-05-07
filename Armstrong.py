# Check if a number is an Armstrong number

num = int(input("Enter a number: "))
num_str = str(num)
power = len(num_str)

# Calculate sum of digits raised to the power
armstrong_sum = sum(int(digit) ** power for digit in num_str)

# Check and print result
if num == armstrong_sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
