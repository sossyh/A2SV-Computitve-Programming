class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heap = []
        
        for i in nums:
            if len(self.heap) < self.k:
                heapq.heappush(self.heap, i)
            
            elif len(self.heap) >= self.k:
                if self.heap[0] < i:
                    heapq.heappop(self.heap)
                    heapq.heappush(self.heap, i)           
        
    def add(self, val: int) -> int:
       
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            
        elif self.heap[0] < val:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        
        return self.heap[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)