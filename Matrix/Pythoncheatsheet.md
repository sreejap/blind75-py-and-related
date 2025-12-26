# initialize 3x3 zero matrix
matrix = [[0]*3 for _ in range(3)]

# access
matrix[0][1]

# iterate
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j])
