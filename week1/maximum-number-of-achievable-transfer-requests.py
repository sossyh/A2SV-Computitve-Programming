class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        indegree = [0] * n

        def backtrack(idx, c):
            if idx >= len(requests):
                balanced = True
                for i in indegree:
                    if i != 0:
                        balanced = False
                return c if balanced else 0

            
            indegree[requests[idx][0]] -= 1
            indegree[requests[idx][1]] += 1

            pick = backtrack(idx + 1, c + 1)

            indegree[requests[idx][0]] += 1
            indegree[requests[idx][1]] -= 1

            dontpick = backtrack(idx + 1, c)
            
            return max(pick, dontpick)
        
        return backtrack(0, 0)