def repeat(par):
    return [num for num in set(par) if par.count(num) > 1]

numbers = list(map(int, input("Enter numbers: ").split(',')))
print(repeat(numbers))
