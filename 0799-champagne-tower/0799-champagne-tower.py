class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        @cache
        def dp(row, col):
            if poured == 0:
                return 0
            
            if row == 0:
                return poured
            
            prevrow = row - 1
            parent1, parent2 = 0, 0
            if col-1 >= 0:
                parent1 = dp(row-1, col-1)
            
            if col <= prevrow:
                parent2 = dp(row-1, col)
            
            if parent1 > 1:
                parent1 -= 1
            else:
                parent1 = 0
            if parent2 > 1:
                parent2 -= 1
            else:
                parent2 = 0
            
            mine = (parent1 / 2) + (parent2 / 2)
            
            return mine
        
        ans = dp(query_row, query_glass)
        
        return 1 if ans >= 1 else ans
       