class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(0)
        stack = []
        total = 0
        
        for i in range(len(arr)):
            curr_lb = i - 1
            while stack and arr[stack[-1][1]] > arr[i]:
                prev, curr = stack.pop()
                left = curr - prev
                right = i - curr
                freq = (right * left)
                total += freq * arr[curr]
                curr_lb = prev
            
            stack.append((curr_lb, i))
        
        return (total) % (pow(10, 9) + 7)