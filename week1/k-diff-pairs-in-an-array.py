class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        count = 0

        for num in nums:
            hashmap[num] += 1
        
        if k == 0:
            for key in hashmap:
                if hashmap[key] > 1:
                    count += 1
        else:
            for key in hashmap:
                if key - k in hashmap:
                    count += 1
        
        return count


        