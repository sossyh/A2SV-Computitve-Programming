class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        problem: to find the longest non-decresearing subsequence

        Solution: 1. will use DP - explore every possiblities
                  2. at a given i choose both and see the one which gives the longest subsequence
        
        1. state - idx
        2. basecase - idx >= len(nums1)
        3. recurence relation - calling the dp function idx + 1
        4. memoization

        example:
                nums1 = [2,3,1], nums2 = [1,2,1]

                [2,] - [2,3] - [2,3,1] - 2
                             - [2, 3, 1] - 2
                     - [2, 2] - [2, 2, 1] - 2
                              - [2, 2, 1] 2
                [1,] - [1,2] - [1,2,1] 2
                             - [1, 2, 1] 2
                     - [1,3] -[1, 3, 1] 2
                             - [1, 3, 1] 2
                
        
        complexties:
                    N = len(nums1)
                    TC: O(2N) - O(N)
                    SP: O(N) + O(N) - O(N)

        """

        memo = {}


        def dp(idx, prev):
            if (idx, prev) in memo:
                return memo[(idx, prev)]
            
            if idx >= len(nums1):
                return 0
            

            longest_subsequence = 0

            if not prev:
                longest_subsequence = dp(idx + 1, prev)
            
            if prev <= nums1[idx]:
                longest_subsequence = max(longest_subsequence, dp(idx + 1, nums1[idx]) + 1)
            
            if prev <= nums2[idx]:
                longest_subsequence = max(longest_subsequence, dp(idx + 1, nums2[idx]) + 1)


            
            memo[(idx, prev)] = longest_subsequence
            return longest_subsequence
        
        return dp(0, 0)

                
                






















