class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = -piles[i]
        
        heapify(piles)
        
        for i in range(k):
            a = heappop(piles)
            heappush(piles, a // 2)
        
        return -sum(piles)