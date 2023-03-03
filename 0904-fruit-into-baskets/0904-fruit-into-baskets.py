class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        d = {}
        max_ = float("-inf")
        
        for end in range(len(fruits)):
            if fruits[end] not in d:
                d[fruits[end]] = 0
            d[fruits[end]] += 1
            while len(d) > 2:
                d[fruits[start]] -= 1
                if d[fruits[start]] == 0:
                    del d[fruits[start]]
                start += 1
            max_ = max(max_, end - start + 1)
        
        return max_
            
                