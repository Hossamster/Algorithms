from math import inf
matrix = [[0,9,-4,inf],[6,0,inf,2],[inf,5,0,inf],[inf,inf,1,0]]

# for row in matrix:
#     for col in row:
#         print(col)
# print(matrix)


m = len(matrix)
# print(m)

for i in range(0,m):
    for j in range(0,m):
        for k in range(0,m-1):
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]
print(matrix)
