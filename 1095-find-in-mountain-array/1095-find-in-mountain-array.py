# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        # finding the peek
        n = mountain_arr.length() - 1
        low, high = 0, n
        peek = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            expected = mountain_arr.get(mid)
            prev, nxt = None, None
            if mid != 0:
                prev = mountain_arr.get(mid - 1)
                
            if mid != mountain_arr.length() - 1:
                nxt = mountain_arr.get(mid + 1)
        
            
            if prev != None and nxt != None and expected > prev and expected > nxt:
                    peek = mid
                    break
            
            elif prev == None:
                low = mid + 1
            
            elif nxt == None:
                high = mid - 1
            
            elif prev < expected and expected < nxt:
                low = mid + 1
            
            else:
                high = mid - 1
        
        # checking if the peek equals to the target
        if mountain_arr.get(peek) == target:
            return peek
        
        
        # finding form the left part
        low, high = 0, peek - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            expected = mountain_arr.get(mid)
            if expected == target:
                return mid
            
            elif expected < target:
                low = mid + 1
            
            else:
                high = mid - 1
        
        
        # finding form the right
        low, high = peek + 1, n
        
        while low <= high:
            mid = low + (high - low) // 2
            
            expected = mountain_arr.get(mid)
            if expected == target:
                return mid
            
            elif expected < target:
                high = mid - 1
            
            else:
                low = mid + 1
        
        
        # non available
        return -1
            