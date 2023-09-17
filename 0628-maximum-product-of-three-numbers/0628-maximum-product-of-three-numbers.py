class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        twosmaller = heapq.nsmallest(2, nums)
        threelargest = heapq.nlargest(3, nums)
        
        positives = threelargest[0] * threelargest[1] * threelargest[2]
        
        negatives = twosmaller[0] * twosmaller[1] * threelargest[0]
        
        return max(positives, negatives)
            
        