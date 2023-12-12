class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bitset = ["0"] * size
        self.one_count = 0
        self.flip_count = 0

    def fix(self, idx: int) -> None:
        if self.flip_count % 2 == 0:
            if self.bitset[idx] == "1":
                return

            self.bitset[idx] = "1"
            self.one_count += 1
        
        else:
            if self.bitset[idx] == "0":
                return

            self.bitset[idx] = "0"
            self.one_count -= 1

    def unfix(self, idx: int) -> None:
        if self.flip_count % 2 == 0:
            if self.bitset[idx] == "0":
                return

            self.bitset[idx] = "0"
            self.one_count -= 1
        
        else:
            if self.bitset[idx] == "1":
                return

            self.bitset[idx] = "1"
            self.one_count += 1

        

    def flip(self) -> None:
        self.flip_count += 1

    def all(self) -> bool:
        return self.one_count == self.size if self.flip_count % 2 == 0 else self.size - self.one_count == self.size
        

    def one(self) -> bool:
        return self.one_count >= 1 if self.flip_count % 2 == 0 else self.size - self.one_count >= 1
        

    def count(self) -> int:
        return self.one_count if self.flip_count % 2 == 0 else self.size - self.one_count
        

    def toString(self) -> str:
        if self.flip_count % 2 == 0:
            return "".join(self.bitset)
        
        ans = ""

        for bit in self.bitset:
            if bit == "0":
                ans += "1"
            else:
                ans += "0"
        
        return ans
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()


"""
problem: implement bitset class

Solution:
1. list - bitset, class - one_count
2. initialising - biset - with all zeros for the given size
3. fix - change 0 - 1 in the given idx, one_count += 1
4. unfix - change 1 to 0 and decrease one_count -= 1
5. iterate over bitset and change 1 to 0 and 0 to 1, if 1 to 0 will decrese one_count by 1 and 
                                                     if 0 to 1 will increse one_count by 1
6. all - one_count == size -- true else false 
7. one - if one_count >= 1 -- true else false
8. count - return one_count
9. tostirng - join the list


Example:
["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"]
[[5], [3], [1], [], [], [0], [], [], [0], [], []]

c = 2

[0, 1, 0, 1, 0]

[0, 0, 1, 0, 1]

[0, 1, 0, 1, 0]


complexty analysis

TC: BITSET - O(1)
    FIX - O(1)
    UNFIX - O(1)
    FLIP - O(N)
    ALL - O(1)
    ONE - O(1)
    COUNT - O(1)
    TOSTRING - O(N)

SP: O(SIZE)



"""