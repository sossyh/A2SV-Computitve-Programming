class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_ = max(nums)
        min_ = min(nums)

        return 0 if (max_ - k) - (min_ + k) <= 0 else (max_ - k) - (min_ + k)
        
        
                                                                                                            
                    