class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = deque()
        
        for end in range(len(nums)):
            while queue and nums[queue[-1]] < nums[end]:
                queue.pop()
            queue.append(end)
            
            if end >= k-1:
                while queue[0] < end + 1 - k:
                    queue.popleft()
                
                result.append(nums[queue[0]])

                
        return result
