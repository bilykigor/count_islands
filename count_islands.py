def count_islands(matrix):
    if not matrix:
        return 0
    
    m,n = len(matrix), len(matrix[0])

    def dfs(i, j):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == 0:
            return
        matrix[i][j] = 0
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    num_islands = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                num_islands += 1
                dfs(i, j)

    return num_islands

if __name__ == '__main__':
    matrixes =  [
    [[0,1,0],
    [0,0,0],
    [0,1,1]],
             
    [[0,0,0,1],
    [0,0,1,0],
    [0,1,0,0]],
    
    [[0,0,0,1],
    [0,0,1,1],
    [0,1,0,1]]
    ]
    
    for matrix in matrixes:
        print(count_islands(matrix))