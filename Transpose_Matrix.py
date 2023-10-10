def transpose_matrix(matrix):
    n= len(matrix)
    m= len(matrix[0])
    
    transposed_matrix = [[0 for j in range(n)] for i in range(m)]
    
    for i in range(0,n):
        for j in range(0,m):
            transposed_matrix[i][j]=matrix[j][i]
            
    return transposed_matrix

matrix=[[1,2,3],[4,5,6],[7,8,9]]

print(matrix)
print(transpose_matrix(matrix))