class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        visited = [False for i in range(k)]
        
        for i in range(len(nums) - 1, -1 , -1):
            if 0 < nums[i] <= k:
                visited[nums[i]-1] = True
            
            operations += 1
            
            all_visited = True
            for i in visited:
                if not i:
                    all_visited = False
            
            
            if all_visited:
                return operations
                
            
                
            