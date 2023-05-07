class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = deque()
        heap = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sum_ = nums1[i] + nums2[j]
                if len(heap) < k:
                    heappush(heap, (-sum_, nums1[i], nums2[j]))
                elif sum_ < -heap[0][0]:
                    heappop(heap)
                    heappush(heap, (-sum_, nums1[i], nums2[j]))
                else:
                    break
                    
        while heap:
            a, b, c = heappop(heap)
            result.appendleft([b,c])
        
        return result