class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = Counter(nums)
        result = []
        
        for i in freq:
            heappush(heap, (-freq[i], i))
        
        while k:
            a = heappop(heap)
            result.append(a[1])
            k -= 1
        
        return result