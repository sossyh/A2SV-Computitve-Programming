class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapify(stones)
        while len(stones) > 1:
            y = -heappop(stones)
            x = -heappop(stones)
            if x == y:
                continue
            if y > x:
                heappush(stones, x-y)
                
        return -stones[0] if len(stones) == 1 else 0


        # if len(stones) == 1:
        #     return -stones[0] 
        # if len(stones) == 0:
        #     return 0
        
        # heapify(stones)
        # y = -heappop(stones)
        # x = -heappop(stones)

        # if x == y:
        #     self.lastStoneWeight(stones)
        # if y > x:
        #     heappush(stones, y-x)
        #     self.lastStoneWeight(stones)