class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(0)
        summ = 0
        stack = []
        
        for i in range(len(arr)):
            currlb = i - 1
            
            while stack and arr[stack[-1][1]] > arr[i]:
                element = stack.pop()
                
                leftspan = element[1] - element[0]
                rightspan = i - element[1]
                
                freq = leftspan * rightspan
                
                summ += freq * arr[element[1]]
                
                currlb = element[0]
                
            
            
            stack.append((currlb, i))
        
        return summ % (pow(10,9)+7)
                