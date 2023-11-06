class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        freq = Counter(nums)
        
        while freq:
            grp = k
            start = min(freq.keys())
            
            while grp:
                if start not in freq:
                    return False
                
                freq[start] -= 1
                if freq[start] == 0:
                    del freq[start]
                
                start += 1
                grp -= 1
        
        return True