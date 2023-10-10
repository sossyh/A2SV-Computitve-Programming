class Solution:
    def build_graph(self, equations, values):
        graph = defaultdict(list)
        
        for k in range(len(values)):
            i, j = equations[k]
            graph[i].append((j, values[k]))
            graph[j].append((i, 1 / values[k]))
        
        return graph
    
    def find_value(self, a, b, total, visited):
        
        if self.graph[a] == []:
            return -1
        
        if a == b:
            return total
        
        visited.add(a)
        
        value = -1
        
        for nbr in self.graph[a]:
            if nbr[0] not in visited:
                a = self.find_value(nbr[0], b, total * nbr[1], visited)
                value = max(value, a)
        
        return value
        
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph = self.build_graph(equations, values)
        result = []
        
        for i, j in queries:
            a = self.find_value(i, j, 1, visited = set())
            result.append(a)
        
        return result