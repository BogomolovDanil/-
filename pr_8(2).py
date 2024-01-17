def replace_max_min_elements(matrix):
    for row in matrix:
        # Находим индексы максимального и минимального элементов в строке
        max_index = row.index(max(row))
        min_index = row.index(min(row))

        # Меняем местами максимальный элемент с первым элементом строки
        row[0], row[max_index] = row[max_index], row[0]

        # Меняем местами минимальный элемент с последним элементом строки
        row[-1], row[min_index] = row[min_index], row[-1]


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

replace_max_min_elements(matrix)


for row in matrix:
    print(row)
