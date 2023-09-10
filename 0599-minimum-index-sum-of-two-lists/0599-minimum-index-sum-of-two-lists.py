class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        d = {}
        
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    d[list1[i]] = i+j
                    
        
        minfreq = inf
        
        for i in d:
            minfreq = min(d[i], minfreq)
        
        for i in d:
            if d[i] == minfreq:
                ans.append(i)
                
        return ans