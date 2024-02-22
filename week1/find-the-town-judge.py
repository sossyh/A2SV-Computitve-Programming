class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i, j in trust:
            graph[i].append(j)
        
        candidate = -1
        for i in range(1, n + 1):
            if i not in graph:
                candidate = i
                break
        
        count = 0
        for node in graph:
            if candidate in graph[node]:
                count += 1
        
        return candidate if count == n - 1 else -1
            
        
