# Program to matrix multiplication
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
Y = [[5, 4, 3],
     [2, 8, 7],
     [1, 1, 2]]
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for i in range(len(X)):
    for j in range(len(Y)):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
for r in result:
    print(r)