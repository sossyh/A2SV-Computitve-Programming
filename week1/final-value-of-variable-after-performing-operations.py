class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0

        for x, y, z in operations:
            if y == '-':
                ans -= 1
            
            else:
                ans += 1
        
        return ans