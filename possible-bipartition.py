class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        colors = [None for i in range(n+1)]
        graph = defaultdict(list)
        ans = True

        for i in dislikes:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        def dfs(vertex, color):
            if colors[vertex] == None:
                colors[vertex] = color
            else:
                return True if colors[vertex] == color else False

            newcolor = 0 if color == 1 else 1

            for i in graph[vertex]:
                if not dfs(i, newcolor):
                    return False
            
            return True

        for i in range(1, n+1):
            if colors[i] == None:
                if not dfs(i, 0):
                    return False

        return True