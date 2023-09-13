class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        visited = set()
        
        for i, j in nums:
            for k in range(i, j+1):
                visited.add(k)
        
        return len(visited)
        