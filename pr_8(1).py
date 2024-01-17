def sum_positive_above_diagonal(matrix):
    N = len(matrix)
    sum_above_diagonal = 0
    count_positive_elements = 0

    for i in range(N):
        for j in range(i+1, N):
            if matrix[i][j] > 0:
                sum_above_diagonal += matrix[i][j]
                count_positive_elements += 1

    return sum_above_diagonal, count_positive_elements

# Пример матрицы A[N, N]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result_sum, result_count = sum_positive_above_diagonal(matrix)
print(f"Сумма положительных элементов над главной диагональю: {result_sum}")
print(f"Число положительных элементов над главной диагональю: {result_count}")

