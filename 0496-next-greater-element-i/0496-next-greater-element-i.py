class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums2)
        stack = []
        d = {nums2[i] : i for i in range(len(nums2))}
        
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                idx = stack.pop()
                result[idx] = nums2[i]
            
            stack.append(i)
        
        
        res = [-1] * len(nums1)
        
        for i in range(len(nums1)):
            elem = nums1[i]
            idx = d[elem]
            res[i] = result[idx]
        
        return res
        
        

        