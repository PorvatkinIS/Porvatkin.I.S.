def swap_max_diagonal_elements(matrix):
    n = len(matrix)
    max_val = matrix[0][0]
    max_i, max_j = 0, 0

    
    for i in range(n):
        if matrix[i][i] > max_val:
            max_val = matrix[i][i]
            max_i, max_j = i, i
        if matrix[i][n - 1 - i] > max_val:
            max_val = matrix[i][n - 1 - i]
            max_i, max_j = i, n - 1 - i

    
    matrix[max_i][max_j], matrix[max_j][max_i] = matrix[max_j][max_i], matrix[max_i][max_j]

    return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result_matrix = swap_max_diagonal_elements(matrix)
print("Измененная матрица:")
for row in result_matrix:
    print(row)
