class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        def helper(arr, r, l):
            while l <  r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        n = len(nums)-1
        helper(nums,n,0)
        helper(nums,k-1,0)
        helper(nums,n,k)