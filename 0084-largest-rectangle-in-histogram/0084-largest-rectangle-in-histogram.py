class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        gmax = 0
        stack = []
        
        for i in range(len(heights)):
            curr_lb = i - 1
            while stack and heights[stack[-1][0]] >heights[i]:
                val = stack.pop()
                left = val[1]
                curr_lb = left
                right = i
                area = heights[val[0]] * (right - left - 1)
                gmax = max(gmax, area)
                
            stack.append((i, curr_lb))
                
        return gmax
            