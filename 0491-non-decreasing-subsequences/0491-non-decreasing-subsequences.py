class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = set()
        
        def backtrack(lst, idx):
            if len(lst) >= 2 and tuple(lst) not in visited and lst == sorted(lst):
                visited.add(tuple(lst))
                result.append(lst[:])
            
            for i in range(idx,len(nums)):
                    lst.append(nums[i])
                    backtrack(lst, i + 1)
                    lst.pop()
                
                    
        backtrack([], 0)
        
        return result
        