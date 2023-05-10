class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        count = [0 for i in range(n)]
        graph = defaultdict(list)
        result = [set() for i in range(n)]
        queue = deque()

        for pre, node in edges:
            graph[pre].append(node)
            count[node] += 1
        
        # def dfs(vertex, parent):
        #     if graph[vertex] == []:
        #         result[vertex] += parent
        #         return 
        #     for i in graph[vertex]:
        #         parent
        #         dfs(i, )

        for i in range(n):
            if count[i] == 0:
                queue.append(i)
        
        while queue:
            item = queue.popleft()
            for i in graph[item]:
                a = set()
                a.add(item)
                result[i] = result[i] | result[item] | a
                count[i] -= 1
                if count[i] == 0:
                    queue.append(i)

        for i in range(n):
            result[i] = sorted(list(result[i]))
            
        return result