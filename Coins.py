def coins(grid):
    N = len(grid)
    M = len(grid[0]) if N > 0 else 0
    
    dp = [[0] * M for _ in range(N)]
    dp[0][0] = grid[0][0]

    for j in range(1, M):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = grid[i][j] + max(dp[i-1][j], dp[i][j-1])

    return dp[N-1][M-1]

# Example 
if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    result = coins(grid)
    print("Largest number of coins collected is:", result)
