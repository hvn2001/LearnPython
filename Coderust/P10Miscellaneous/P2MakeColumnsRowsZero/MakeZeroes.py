def print_matrix(m):
    print()
    for l in m:
        for x in l:
            print(x, end='\t')
        print()


def make_zeroes(matrix):
    if not matrix:
        return

    zero_rows = set()
    zero_cols = set()

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(0, rows):
        for j in range(0, cols):
            if matrix[i][j] == 0:
                if i not in zero_rows:
                    zero_rows.add(i)
                if j not in zero_cols:
                    zero_cols.add(j)

    for r in zero_rows:
        for c in range(0, cols):
            matrix[r][c] = 0

    for c in zero_cols:
        for r in range(0, rows):
            matrix[r][c] = 0


def is_row_or_col_zero(matrix, r, c):
    if not matrix:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(0, cols):
        if matrix[r][i] == 0:
            return True

    for i in range(0, rows):
        if matrix[i][c] == 0:
            return True

    return False


matrix = [
    [5, 4, 3, 9],
    [2, 0, 7, 6],
    [1, 3, 4, 0],
    [9, 8, 3, 4]
]
print("Orginal Matrix", end="")
print_matrix(matrix)
make_zeroes(matrix)
print("\nMatrix with Zeros", end="")
print_matrix(matrix)
