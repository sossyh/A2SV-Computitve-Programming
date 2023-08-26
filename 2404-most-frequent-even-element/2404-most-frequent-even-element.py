class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = Counter(nums)
        candid = []
        
        maxfreq = -1
        
        for i in freq:
            if i % 2 == 0:
                maxfreq = max(maxfreq, freq[i])
        
        if maxfreq == -1:
            return -1
        
        for i in freq:
            if i % 2 == 0 and freq[i] == maxfreq:
                candid.append(i)
        
        candid.sort()
        
        return candid[0]
    
            