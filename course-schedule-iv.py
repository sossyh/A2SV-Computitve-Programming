class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        isReachable = defaultdict(set)
        graph = defaultdict(list)
        incoming = [0 for i in range(numCourses)]
        queue = deque()
        result = []

        for pre, cou in prerequisites:
            graph[pre].append(cou)
            incoming[cou] += 1
        
        for i in range(numCourses):
            if incoming[i] == 0:
                	queue.append(i)
        
        while queue:
            item = queue.popleft()
            for i in graph[item]:
                a = set([item])
                isReachable[i] = isReachable[item] | isReachable[i] | a
                incoming[i] -= 1
                if incoming[i] == 0:
                    queue.append(i)
        
        for i, j in queries:
            if i in isReachable[j]:
                result.append(True)
            else:
                result.append(False)
        
        return result