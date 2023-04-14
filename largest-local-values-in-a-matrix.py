class Solution:
    def maxelement(self, grid):
        flatten = []
        for i in range(len(grid)):
            flatten += grid[i]
        return max(flatten)

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = [[0] * (len(grid)-2) for i in range(len(grid)-2)]

        for i in range(len(result)):
            for j in range(len(result)):
                newgrid = [ l[j: j+3] for l in grid[i : i + 3]]
                maxe = self.maxelement(newgrid)
                result[i][j] = maxe

        return result