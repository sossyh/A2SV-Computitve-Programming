from typing import List
class Solution:
    def helper(self, vertex, adj, parent, visited):
        if vertex in visited:
            return True
        
        visited.add(vertex)
        for i in adj[vertex]:
            if i != parent:
                if self.helper(i, adj, vertex, visited):
                    return True
        
        return False
        
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    visited = set()
	    for i in range(V):
	        if i not in visited:
	            if self.helper(i, adj, None, visited):
	                return 1
	   
	    return 0
	            
	    
		#Code here
