a = [
    [4, 5, 8, 4],
    [4, 8, 6, 7],
    [1, -5, 7, 4]
]


def gaussjordan(matrix, n):
    for i in range(n):
        ab = (n - 1) - i
        ar = (i + 1) - 1
        for j in range(1, ab + 1):
            index = matrix[i][i] / matrix[i + j][i]
            for k in range(n + 1):
                matrix[j + i][k] = matrix[j + i][k] * index
                matrix[j + i][k] = matrix[j + i][k] - matrix[i][k]
        for j in range(ar):
            index = matrix[i][i] / matrix[i - j][i]
            for k in range(n + 1):
                matrix[i - j][k] = matrix[i - j][k] * index
                matrix[i - j][k] = matrix[i - j][k] - matrix[i][k]

    return matrix


print(gaussjordan(a, 3))
