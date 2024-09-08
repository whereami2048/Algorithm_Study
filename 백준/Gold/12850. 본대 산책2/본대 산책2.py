def matrixmult(A, B, mod, k):
    K = [[0 for _ in range(k)] for _ in range(k)]
    for i in range(k):
        for j in range(k):
            ele = 0
            for m in range(k):
                ele += (A[i][m]*B[m][j])%mod
            K[i][j] = ele%mod
    return K
def multiply(A, n, mod, k):
    if n == 1:
        return A

    temp = multiply(A, n//2, mod, k)

    if n % 2 == 0:
        return matrixmult(temp, temp, mod, k)
    else:
        return matrixmult(A, matrixmult(temp, temp, mod, k), mod, k)


D = int(input())

matrix = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 0, 0, 0, 0],
          [1, 1, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 1, 1, 0, 0],
          [0, 0, 1, 1, 0, 1, 0, 1],
          [0, 0, 0, 1, 1, 0, 1, 0],
          [0, 0, 0, 0, 0, 1, 0, 1],
          [0, 0, 0, 0, 1, 0, 1, 0]]

if D == 1:
    print(0)
    exit(0)
else:
    K = multiply(matrix, D, 1000000007, 8)
    print(K[0][0])
    exit(0)
