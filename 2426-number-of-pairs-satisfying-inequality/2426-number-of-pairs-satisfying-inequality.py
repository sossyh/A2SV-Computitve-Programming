class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        merged = []
        new = []
        for i in range(len(nums1)):
            merged.append(nums1[i] - nums2[i])
        
        def mergesort(left, right):
            if left == right:
                return [0, [merged[left]]]
            
            mid = left + (right - left)//2
            leftcount, leftarr = mergesort(left, mid)
            rightcount, rightarr = mergesort(mid+1, right)
            ans = leftcount + rightcount
            n = len(rightarr)
            for num in leftarr:
                ans += (n-bisect_left(rightarr, num - diff))
            
            return [ans, sorted(leftarr+rightarr)]
        
        return mergesort(0, len(merged)-1)[0]
            
        
        
        
        
        
        
        
        
        
        
        
        
        
#         count = 0
#         merged = []
#         new = []
#         for i in range(len(nums1)):
#             merged.append(nums1[i] - nums2[i])
                    
#         def mergesort(arr):
#             nonlocal count
            
#             if len(arr) <= 1:
#                 return arr
              
#             mid = len(arr)//2
#             left = mergesort(arr[:mid])
#             right = mergesort(arr[mid:])
            
            
                
#             i, j = (len(left) - 1), 0
#             while j < len(right):
#                 while i >= 0:
#                         if left[i] <= right[j] + diff:
#                             count += (i + 1)
#                             break
#                         i -= 1  
#                 j += 1
                        
                  
#             # l,r = 0,0
# #             while l < len(left) and r < len(right):
# #                     if left[l] < right[r]:
# #                         new.append(left[l])
# #                         l += 1
# #                     else:
# #                         new.append(right[r])
# #                         r += 1
                        
# #             while l < len(left):
# #                         new.append(left[l])
# #                         l += 1
                
# #             while r < len(right):
# #                     new.append(right[r])
# #                     r += 1
                
#             return sorted(left+right)
            
#         print(mergesort(merged))
            
#         return count

                
                        
                        
                    
                
                
        