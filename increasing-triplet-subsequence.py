class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1, min2 = float('inf'), float('inf')

        for i in nums:
            if min1 < min2 < i:
                return True
            
            if i > min1:
                min2 = i
            else:
                min1 = i
        
        return False