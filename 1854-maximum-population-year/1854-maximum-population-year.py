class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        max_yr = max([i for k, i in logs])
        min_yr = min([i for i, j in logs])
        length_prefix = max_yr - min_yr + 1
        prefix = [0] * length_prefix
        offset = min_yr
        
        for i, j in logs:
            
            prefix[i - offset] += 1
            prefix[j - offset] -= 1
        
        prefixsum = [prefix[0]]
   
        for i in range(1, len(prefix)):
            prefixsum.append(prefixsum[i - 1] + prefix[i])
        
        max_people_start_year = 0
        max_people = 0
        
        for i in range(len(prefixsum)):
            if prefixsum[i] > max_people:
                max_people_start_year = i
                max_people = prefixsum[i]
        
        return max_people_start_year + offset