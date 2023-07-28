class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = Counter(arr)
        visitedfreq = set()
        
        for i in hashmap:
            if hashmap[i] in visitedfreq:
                return False
            visitedfreq.add(hashmap[i])
        
        return True
            
        