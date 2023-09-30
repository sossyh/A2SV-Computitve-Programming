class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        n = len(nums)
        k = math.floor(n/3)
       
        
        numsFreqMoreThanOneThihrd = []
        
        for num in freq:
            if freq[num] > k:
                numsFreqMoreThanOneThihrd.append(num)
        
        return numsFreqMoreThanOneThihrd