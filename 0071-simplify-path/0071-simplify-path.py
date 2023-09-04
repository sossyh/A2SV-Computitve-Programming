class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = ["/"]
        
        for i in path:
            
            if i and i != ".." and i != ".":
                if stack and stack[-1] != "/":
                    stack.append("/" + i)
                else:
                    stack.append(i)
            
            
            elif stack and stack[-1] != "/" and i == "..":
                stack.pop()
            
            elif i == ".":
                continue
        
        return "".join(stack)
                
                