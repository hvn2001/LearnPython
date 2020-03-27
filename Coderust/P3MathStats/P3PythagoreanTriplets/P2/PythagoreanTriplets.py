def find_pythagorean_triplets(arr):
    n = len(arr)
    triplets = []
    arr.sort()

    for i in range(0, n):
        if arr[i] is 0:
            continue

        c2 = arr[i] ** 2

        j = 0
        k = n - 1

        while j < k:
            if j is i or arr[j] is 0:
                j += 1
                continue

            if k is i or arr[k] is 0:
                k -= 1
                continue

            a2 = arr[j] ** 2
            b2 = arr[k] ** 2

            if a2 + b2 is c2:
                triplets.append([arr[j], arr[k], arr[i]])
                break
            elif a2 + b2 + (-c2) > 0:
                k -= 1
            else:
                j += 1

    return triplets


l1 = [4, 16, 1, 2, 3, 5, 6, 8, 25, 10]
print("Original: ", l1)
t1 = find_pythagorean_triplets(l1)

print("Pythagorean triplets: ", end="")
for x in t1:
    print(str(x), end="")
