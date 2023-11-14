def max_min(matrix):
    max_in_rows = []
    min_in_cols = []
    for row in matrix:
        max_in_rows.append(max(row))
    for j in range(len(matrix[0])):
        column = [matrix[i][j] for i in range(len(matrix))]
        min_in_cols.append(min(column))
    return max_in_rows, min_in_cols


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
max_in_rows, min_in_cols = max_min(matrix)
print("Наибольший элемент в каждой строке:", max_in_rows)
print("Наименьший элемент в каждом столбце:", min_in_cols)
