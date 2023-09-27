class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans, n = [], len(intervals)
        
        intervals.sort()
        ans = [intervals[0]]
        
        for i in range(1, n):
            curr = ans[-1]
            a, b = intervals[i]
            if a <= curr[1] and curr[0] <= a:
                initial = curr[0]
                final = max(b, curr[1])
                ans[-1] = [initial, final]
            else:
                ans.append(intervals[i])
        
        return ans