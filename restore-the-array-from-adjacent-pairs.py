class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        result = []
        visited = set()

        for i, j in adjacentPairs:
            graph[i].append(j)
            graph[j].append(i)

        queue = deque()
        for i in graph:
            if len(graph[i]) == 1:
                queue.append(i)
                visited.add(i)
                result.append(i)
                break
        
        while queue:
            item = queue.popleft()
            for i in graph[item]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
                    result.append(i)
        
        return result