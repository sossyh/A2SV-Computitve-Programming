class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        dirx, diry = 0, 1
        
        for i in instructions:
            
            if i == "R":
                dirx, diry = diry, -dirx
                
            elif i == "L":
                dirx, diry = -diry, dirx
                
            else:
                x, y = x + dirx, y + diry
        
        
        return (x, y) == (0, 0) or (dirx, diry) != (0, 1)