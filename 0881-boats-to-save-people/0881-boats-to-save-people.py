class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r = 0, len(people)-1
        count = 0
        while l <= r:
            if people[r] + people[l] <= limit:
                count += 1
                l += 1
                r -= 1
            else:
                
                count += 1
                r -= 1
        
        return count
                