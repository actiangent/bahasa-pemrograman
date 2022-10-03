matrix_1 = [[17, 21], [31, 19]]
matrix_2 = [[51, 15], [84, 96]]

def add_matrices(first_matrix, second_matrix):
    result = []
    for i in range(len(first_matrix)):
        row = []
        for j in range(len(first_matrix[0])):
            row.append(first_matrix[i][j]+second_matrix[i][j])
        result.append(row)
    return result

for i in add_matrices(matrix_1, matrix_2):
    print(i)