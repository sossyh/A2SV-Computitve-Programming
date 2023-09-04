class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        breaked = 0
        
        for i in asteroids:
            while stack and ( (stack[-1] > 0 and i < 0)):
                    if abs(stack[-1]) == abs(i):
                        stack.pop()
                        breaked = 1
                        break
                    elif abs(stack[-1]) > abs(i):
                        breaked = 1
                        break
                    else:
                        stack.pop()
            
            if not breaked:
                stack.append(i)
                
            breaked = 0
        
        
        return stack