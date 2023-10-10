class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_gas = sum(gas)
        sum_cost = sum(cost)
        
        if sum_cost > sum_gas:
            return -1
        
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        
        total = 0
        start = 0
        for i in range(len(diff)):
            total += diff[i]
            
            if total < 0:
                total = 0
                start = i + 1
            
        return start
            
        