# Чтение матрицы из файла
def read_matrix(file_name):
    with open(file_name, 'r') as file:
        matrix = [[float(num) for num in line.split()] for line in file]
    return matrix

# Нахождение наибольшего элемента на диагоналях и их координат
def find_max_on_diagonals(matrix):
    n = len(matrix)
    max_val = float('-inf')
    max_i, max_j = 0, 0
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                if matrix[i][j] > max_val:
                    max_val = matrix[i][j]
                    max_i, max_j = i, j
    return max_val, max_i, max_j

# Поменять местами наибольший элемент с элементом на пересечении диагоналей
def swap_elements(matrix, i1, j1, i2, j2):
    matrix[i1][j1], matrix[i2][j2] = matrix[i2][j2], matrix[i1][j1]

# Запись результатов в файл
def write_matrix(matrix, output_file):
    with open(output_file, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

# Пример использования
matrix = read_matrix('input.txt')
max_val, max_i, max_j = find_max_on_diagonals(matrix)
center_i, center_j = len(matrix) // 2, len(matrix) // 2
swap_elements(matrix, max_i, max_j, center_i, center_j)
write_matrix(matrix, 'output.txt')
