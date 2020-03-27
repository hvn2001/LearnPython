def is_pythagorean_triplet(a, b, c):
    sqra = a * a
    sqrb = b * b
    sqrc = c * c

    if sqra + sqrb is sqrc:
        return True
    elif sqra + sqrc is sqrb:
        return True
    elif sqrb + sqrc is sqra:
        return True
    else:
        return False


def find_pythagorean_triplets(arr):
    n = len(arr)
    triplets = []
    for i in range(0, n - 2):
        if arr[i] is 0:
            continue

        for j in range(i + 1, n - 1):
            if arr[j] is 0:
                continue

            for k in range(j + 1, n):
                if is_pythagorean_triplet(arr[i], arr[j], arr[k]):
                    triplets.append([arr[i], arr[j], arr[k]])

    return triplets


l1 = [4, 16, 1, 2, 3, 5, 6, 8, 25, 10]
print("Original: ", l1)
t1 = find_pythagorean_triplets(l1)

print("Pythagorean triplets: ", end="")
for x in t1:
    x.sort()
    print(str(x), end="")
