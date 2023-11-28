def read_matrix(file_name):
    with open(file_name, 'r') as file:
        matrix = [[int(num) for num in line.split()] for line in file]
    return matrix

def max_in_rows(matrix):
    max_in_rows = [max(row) for row in matrix]
    return max_in_rows

def min_in_columns(matrix):
    transposed = list(zip(*matrix))
    min_in_columns = [min(col) for col in transposed]
    return min_in_columns

def write_results(max_in_rows, min_in_columns, output_file):
    with open(output_file, 'w') as file:
        for num in max_in_rows:
            file.write(f'Max in row: {num}\n')
        for num in min_in_columns:
            file.write(f'Min in column: {num}\n')

matrix = read_matrix('input.txt')
max_elements = max_in_rows(matrix)
min_elements = min_in_columns(matrix)
write_results(max_elements, min_elements, 'output.txt')