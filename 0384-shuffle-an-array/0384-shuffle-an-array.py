class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def reset(self) -> List[int]:
        return self.nums
        

    def shuffle(self) -> List[int]:
        num = self.nums.copy()
        for i in range(len(num)):
            first = i + random.randint(0, len(self.nums) -1 - i)
        
            num[first], num[i] = num[i], num[first]
            
        return num
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()