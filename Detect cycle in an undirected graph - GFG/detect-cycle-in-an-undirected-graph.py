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


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends