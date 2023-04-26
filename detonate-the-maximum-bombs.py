class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue
                
                distance = math.sqrt(pow((bombs[i][0] - bombs[j][0]), 2) + pow((bombs[i][1] - bombs[j][1]), 2) )
                if bombs[i][2] >= distance:
                    graph[i].append(j)
        
        ans = 0
        count = 0

        def dfs(vertex, visited):
            nonlocal count
            if vertex in visited:
                return

            visited.add(vertex)
            count += 1

            for i in graph[vertex]:
                dfs(i, visited)
        
        for i in graph.copy():
            dfs(i, visited = set())
            ans = max(ans, count)
            count = 0
        
        return ans if ans != 0 else 1