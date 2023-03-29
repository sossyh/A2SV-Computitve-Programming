class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        
        
        def mergesort(arr):
            nonlocal count
            
            if len(arr) <= 1:
                return arr
            
            mid = len(arr)//2
            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])
            
            j = 0
            while j < len(right):
                ans = len(left) - bisect_right(left, (right[j]*2))
                count += ans
                j += 1
            
            new = []
            l, r = 0, 0
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    new.append(left[l])
                    l += 1
                else:
                    new.append(right[r])
                    r += 1
            
            while l < len(left):
                new.append(left[l])
                l += 1 
            
            while r < len(right):
                new.append(right[r])
                r += 1
            
            return new
        
        mergesort(nums)
        
        return count
                
                
            
            
        
        
        