class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        1. find runing sum
        2. have runnin sum % k in the hashmap with the frequency
        3. iterate ove the hashmap if hashmap[key] == 0 incresae the total count by hashmap[key]
                                   elif hashmap[key] >= 2 sue the formula to calculate the number of subarrays it can form - formula[(n * n - 1) // 2] n - hashmap[key]
        4. return count        
        
        """

        hashmap = defaultdict(int)
        prefixsumm = 0
        count = 0
        hashmap[0] = 1

        for num in nums:
            prefixsumm += num

            count += hashmap[prefixsumm % k]
            hashmap[prefixsumm % k] += 1

        
        return count
