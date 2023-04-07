class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count = 0
        first, second = edges[0][0], edges[0][1]
        for i in range(1, len(edges)):
            item = edges[i]
            if first == item[1] or first == item[0]:
                return first
            else:
                return second
        