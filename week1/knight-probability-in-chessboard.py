class Solution:
    def isInBound(self, r, c, n):
        return 0 <= r < n and 0 <= c < n

    def dfs(self, row, col, k, n, memo):
        if (row, col, k) in memo:
            return memo[(row, col, k)]

        if k == 0:
            return 1
        
        # visited.add((row, col))
        
        directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        total_moves = 0
        for i, j in directions:
            new_r = row + i
            new_c = col + j

            if self.isInBound(new_r, new_c, n):
                total_moves += self.dfs(new_r, new_c, k - 1, n, memo)  
                # print(new_r, new_c, total_moves)      
        
        memo[(row, col, k)] = total_moves
        return total_moves


    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        total_moves = self.dfs(row, column, k, n, memo = {})
        # print(total_moves)
        total_posibilites = 8 ** k
        probability = total_moves / total_posibilites

        return probability
        


        