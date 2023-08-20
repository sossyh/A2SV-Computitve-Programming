class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0
        nums = [i+1 for i in range(n)]
        visited = 0
        
        def permute(idx):
            nonlocal count, visited
            if idx == n:
                count += 1
                return
            
            for i in range(n):
                
                if not (visited & (1<<i)) and (nums[idx] % (i+1) == 0 or (i+1) % nums[idx] == 0):
                    visited |= (1<<i)
                    permute(idx+1)
                    visited ^= (1<<i)
        
        permute(0)
        
        return count