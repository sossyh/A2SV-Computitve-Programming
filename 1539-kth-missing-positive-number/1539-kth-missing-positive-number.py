class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr = set(arr)
        
        num = 1
        i = 1
        while i <= k:
            if i == k and num not in arr:
                return num
            
            if num not in arr:
                num += 1
                i += 1
            else:
                num += 1
        
        
            
            