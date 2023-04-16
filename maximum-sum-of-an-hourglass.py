class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxsum = -float("inf")
        n, m = len(grid), len(grid[0])

        for i in range(1,n-1):
            for j in range(1,m-1):
                sum_ = sum(grid[i-1][j-1:j+2]) + grid[i][j] + sum(grid[i+1][j-1:j+2])
                maxsum = max(maxsum,sum_)

        return maxsum