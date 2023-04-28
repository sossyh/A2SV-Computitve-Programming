class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)

        for i, j in edges:
            tree[i].append(j)
            tree[j].append(i)

        visited = set()
        
        def dfs(vertex):
            if tree[vertex] == []:
                if hasApple[vertex] and vertex != 0:
                    return 2
                else:
                    return 0

            visited.add(vertex)
            ans = 0
            for i in tree[vertex]:
                if i not in visited:
                    ans += dfs(i)
            
            if vertex != 0 and(ans or hasApple[vertex]):
                return ans + 2
            
            return ans

        return dfs(0)