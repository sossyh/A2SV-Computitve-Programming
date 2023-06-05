class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def backtracking(idx, lst):
            if idx >= len(nums):
                answer.append(lst[:])
                return
            
            lst.append(nums[idx])
            backtracking(idx + 1, lst)
            lst.pop()
            backtracking(idx + 1, lst)
        
        backtracking(0, [])
    
        return answer