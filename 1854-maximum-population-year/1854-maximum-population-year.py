class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        prefix = [0] * 2051
        
        for i, j in logs:
            prefix[i] += 1
            prefix[j] -= 1
        
        prefixsum = [prefix[0]]
        
        for i in range(1, 2051):
            prefixsum.append(prefixsum[i - 1] + prefix[i])
        
        max_people_start_year = 0
        max_people = 0
        
        for i in range(2051):
            if prefixsum[i] > max_people:
                max_people_start_year = i
                max_people = prefixsum[i]
        
        return max_people_start_year