# mat1 = [[int(input()) for i in range(n)] for j in range(n)]
# mat2 = [[int(input()) for i in range(n)] for j in range(n)]
mat1 = [[1, 2, 3,],
       [4, 5, 6],
       [7, 8, 9]]
mat2 = [[1, 2, 3,],
       [4, 5, 6],
       [7, 8, 9]]
mat_sum = [[(mat1[i][j] + mat2[i][j]) for i in range(len(mat1))] for j in range(len(mat1))]
print(mat_sum)
mat_