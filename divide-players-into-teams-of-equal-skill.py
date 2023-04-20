class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill) - 1
        result = []
        start = skill[l] + skill[r]
        while l < r:
            if skill[r] + skill[l] == start:
                result.append(skill[r]*skill[l])
                l += 1
                r -= 1
            else:
                return -1
        return sum(result)