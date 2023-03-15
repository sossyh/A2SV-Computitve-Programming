class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(0)
        sums = 0
        stack = []
        
        for i in range(len(arr)):
            currlb = i - 1
            while stack and arr[stack[-1][0]] > arr[i]:
                val = stack.pop()
                left = val[0] - val[1] 
                currlb = val[1]
                right = i - val[0]
                freq = left * right
                sums += arr[val[0]] * freq
                
            stack.append((i, currlb))
            
        sums = sums % (pow(10,9) + 7)
        return sums
                