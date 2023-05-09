class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        count = [0 for i in range(numCourses)]
        queue = deque()
        toporder = []

        for course, pre in prerequisites:
            graph[pre].append(course)
            count[course] += 1
        
        for i in range(len(count)):
            if count[i] == 0:
                queue.append(i)
        
        while queue:
            item = queue.popleft()
            toporder.append(item)

            for i in graph[item]:
                count[i] -= 1
                if count[i] == 0:
                    queue.append(i)
        
        return True if len(toporder) == numCourses else False