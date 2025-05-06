def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b if b else "Err: /0"

print("1:Add 2:Sub 3:Mul 4:Div")
ch = int(input(">> "))
a, b = int(input("a: ")), int(input("b: "))

print(["Sum", "Sub", "Mul", "Div"][ch-1], "=", [add, sub, mul, div][ch-1](a, b) if 1 <= ch <= 4 else "Invalid")
