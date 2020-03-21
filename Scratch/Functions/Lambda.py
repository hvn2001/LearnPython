# def triple(num): return num * 3  # Assigning the lambda to a variable


triple = lambda num: num * 3

print(triple(10))  # Calling the lambda and giving it a parameter


def concat_strings(a, b, c): return a[0] + b[0] + c[0]


print(concat_strings("World", "Wide", "Web"))


def my_lambda(num): return "High" if num > 50 else "Low"


print(my_lambda(60))
