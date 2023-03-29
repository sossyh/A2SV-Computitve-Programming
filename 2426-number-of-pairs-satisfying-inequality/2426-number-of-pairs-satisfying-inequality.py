class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:        
        count = 0
        merged = []
        
        for i in range(len(nums1)):
            merged.append(nums1[i] - nums2[i])
                    
        def mergesort(arr):
            nonlocal count
            
            if len(arr) <= 1:
                return arr
              
            mid = len(arr)//2
            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])
            
            
                
            j = 0
            while j < len(right):
                ans = bisect_right(left, (right[j]+diff))
                count += ans
                j += 1
                        
            new = []      
            l,r = 0,0
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
            
        print(mergesort(merged))
            
        return count

                
                        
                        
                    
                
                
        