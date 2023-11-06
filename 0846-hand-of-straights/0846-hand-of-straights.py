class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter(hand)
        
        while freq:
            grp = groupSize
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