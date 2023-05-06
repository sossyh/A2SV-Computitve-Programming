class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flattend = []
        heap = []

        for i in matrix:
            flattend += i
        
        for i in flattend:
            if len(heap) < k:
                heappush(heap, -i)

            elif i < -heap[0]:
                heappop(heap)
                heappush(heap, -i)

        return -heap[0]