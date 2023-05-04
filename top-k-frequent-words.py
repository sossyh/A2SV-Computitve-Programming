class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        result = []
        freq = Counter(words)
        heap = []
        
        for i in freq:
            heappush(heap, (-freq[i], i))
        
        for i in range(k):
            a, b = heappop(heap)
            result.append(b)
        
        return result