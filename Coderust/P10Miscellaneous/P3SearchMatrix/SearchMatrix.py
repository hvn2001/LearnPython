def search_in_matrix(matrix, value):
    M = len(matrix)  # rows
    N = len(matrix[0])  # columns

    # Let's start searching from top right
    # Alternatively, searching from bottom left
    # i.e. matrix[M-1][0] can also work

    i = 0
    j = N - 1

    while i < M and j >= 0:
        if matrix[i][j] is value:
            return pair(i, j)
        elif value < matrix[i][j]:
            # search left
            j = j - 1
        else:
            # search down
            i = i + 1

    return pair(-1, -1)


matrix = [
    [2, 4, 9, 13, 15],
    [3, 5, 11, 18, 22],
    [6, 8, 16, 21, 28],
    [9, 11, 20, 25, 31],
]

print("Verifying at ", end="")
result = search_in_matrix(matrix, 8)
print(result.first, ",", result.second, ":", matrix[result.first][result.second])
