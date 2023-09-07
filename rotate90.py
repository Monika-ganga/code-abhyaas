def rotate_matrix(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    matrix[:]=[row[::-1] for row in matrix]
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
rotate_matrix(matrix)
for row in matrix:
    print(row)
