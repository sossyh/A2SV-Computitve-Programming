class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        curr_digit = 0
      
        
        for i in s:
            if i.isnumeric():
                curr_digit = 10 * curr_digit + int(i)
            
            elif i == '[':
                stack.append(curr_digit)
                stack.append("[")
                curr_digit = 0
            
            elif i == "]":
                curr = ""
                while stack and stack[-1] != '[':
                    curr = stack.pop() + curr
                stack.pop()
                freq = stack.pop()
                new_substring = freq * curr
                stack.append(new_substring)
            
            else:
                stack.append(i)
        
        
        return "".join(stack)
                
            