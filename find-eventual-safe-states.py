class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        result = []
        color = [0 for i in range(len(graph))]
    
        def hasCycle(vertex, color):
            
            if color[vertex] == 2:
                return False
            
            if color[vertex] == 1:
                return True
            
            color[vertex] = 1
            for i in graph[vertex]:
                if hasCycle(i, color):
                    return True

            color[vertex] = 2
            return False

        for i in range(len(graph)):
            if not hasCycle(i, color):
                result.append(i)
        
        return result