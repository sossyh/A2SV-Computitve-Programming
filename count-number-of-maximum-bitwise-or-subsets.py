class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        subarrays = []

        def backtracking(idx, lst):
            
            if idx > len(nums) - 1:
                subarrays.append(lst[:])
                return

            lst.append(nums[idx])
            backtracking(idx+1, lst)
            lst.pop()

            backtracking(idx+1, lst)
            
        backtracking(0, [])

        count = defaultdict(int)

        for i in subarrays:
            ors = 0
            for j in i:
                ors = ors | j
            count[ors] += 1
        
        max_ = max(count)
        
        return count[max_]