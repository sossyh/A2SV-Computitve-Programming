class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = {}
        d2 = {}
        ans = []
        
        for i in range(len(list1)):
            d1[list1[i]] = i
        
        for j in range(len(list2)):
            if list2[j] in d1:
                d2[list2[j]] = d1[list2[j]] + j
        
        minif = inf
        
        for i in d2:
            if d2[i] < minif:
                ans = [i]
                minif = d2[i]
            elif d2[i] == minif:
                ans.append(i)
                
        return ans