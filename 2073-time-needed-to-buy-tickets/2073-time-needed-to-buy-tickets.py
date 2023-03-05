class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = []
        count = 0
        
        for i in range(len(tickets)):
            queue.append(i)
        
        while tickets[k] != 0:
            idx = queue.pop(0)
            if tickets[idx] != 0:
                tickets[idx] -= 1
                count += 1  
            queue.append(idx)
        
        return count