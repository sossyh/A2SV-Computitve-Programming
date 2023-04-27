class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        graph = defaultdict(list)
        queue = deque([0])

        for i in range(len(rooms)):
            graph[i] += rooms[i]
        
        while queue:
            item = queue.popleft()
            visited.add(item)
            for i in graph[item]:
                if i not in visited:
                    queue.append(i)
        
        return True if len(visited) == len(rooms) else False