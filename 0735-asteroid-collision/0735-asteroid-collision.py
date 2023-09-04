class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
 
        
        for a in asteroids:
            while stack and ( (stack[-1] > 0 and a < 0)):
                    if abs(stack[-1]) == abs(a):
                        stack.pop()
                        a = 0
                    elif abs(stack[-1]) > abs(a):
                        a = 0
                    else:
                        stack.pop()
            
            if a != 0:
                stack.append(a)
                
           
        return stack