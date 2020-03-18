num = 20


def multiply_by_10(n):
    n *= 10  # immutable data, the function can modify it, data will remain unchanged outside the function’s scope
    # immutable data are numbers, strings, etc.
    num = n  # Changing the value inside the function
    print(num)
    return n


multiply_by_10(num)
print(num)  # The original value remains unchanged
