class Solution:
    def candy(self, ratings: List[int]) -> int:
        ansl = [1 for _ in range(len(ratings))]
        ansr = [1 for _ in range(len(ratings))]

        # left
        for l in range(1, len(ratings)):
            if ratings[l] > ratings[l-1]:
                ansl[l] = ansl[l-1] + 1
        
        # right
        for r in range(len(ratings)-2, -1, -1):
            if ratings[r] > ratings[r+1]:
                ansr[r] = ansr[r+1] + 1
        
        total = 0
        for i in range(len(ratings)):
            total += max(ansl[i], ansr[i])

        return total