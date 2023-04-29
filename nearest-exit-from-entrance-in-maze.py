class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def isInBound(r, c):
            return 0 <= r < len(maze) and 0 <= c < len(maze[0])
        
        def isBoarder(r, c):
            return r == 0 or r == len(maze) -1 or c == 0 or c == len(maze[0])-1
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        visited.add(tuple(entrance))
        entrance.append(0)
        queue = deque()
        queue.append(tuple(entrance))

        while queue:
            item = queue.popleft()
            
            for i, j in directions:
                newr = item[0] + i
                newc = item[1] + j
                if isInBound(newr, newc) and (newr, newc) not in visited and maze[newr][newc] == ".":
                    if isBoarder(newr, newc):
                        return item[2] + 1
            
                    queue.append((newr, newc, item[2] + 1))
                    visited.add((newr, newc))
        
        return -1