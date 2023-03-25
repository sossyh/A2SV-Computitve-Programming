class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # if len(nums) == 1 and k == 1:
        #     return nums[0]
        n = len(nums)
        ans = 0
        def quick(nums, start, end):
            nonlocal ans
            if end - start <= 0:
                if n - k == start:
                    ans = nums[start]
                return
            
            pivot = nums[start]
            write = start + 1
            
            for read in range(start + 1, end + 1):
                if nums[read] <= pivot:
                    nums[write], nums[read] = nums[read], nums[write]
                    write += 1
            
            nums[write-1], nums[start] = nums[start], nums[write-1]
            
            if n - k < write - 1:
                quick(nums, start, write -2)
                
            elif n - k > write - 1:
                quick(nums, write, end)
                
            else:
                ans = nums[n-k]
                
        quick(nums, 0, n-1)
        
        return ans
        
        
        
                
                
        