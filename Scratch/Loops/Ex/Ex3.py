def fib(n):
    if n <= 0:
        return -1
    if n == 1:
        return 0
    if n == 2:
        return 1
    prev1 = 0
    prev2 = 1
    ans = 0
    for i in range(3, n + 1):
        ans = prev1 + prev2
        prev1 = prev2
        prev2 = ans
    return ans


def fib2(n):
    # The first and second values will always be fixed
    first = 0
    second = 1

    if n < 1:
        return -1

    if n == 1:
        return first

    if n == 2:
        return second

    count = 3  # Starting from 3 because we already know the first two values
    while count <= n:
        fib_n = first + second
        first = second
        second = fib_n
        count += 1  # Increment count in each iteration
    return fib_n


n = 7
print(fib(n))
print(fib2(n))
