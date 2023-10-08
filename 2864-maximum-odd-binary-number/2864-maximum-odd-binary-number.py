class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_zeros = 0
        count_ones = 0
        
        for i in s:
            if i == '1':
                count_ones += 1
            else:
                count_zeros += 1
        
        big_odd_num = deque()
        
        if count_ones:
            big_odd_num.append('1')
            count_ones -= 1
        
        if count_zeros:
            zeros = '0' * count_zeros
            big_odd_num.appendleft(zeros)
            
        if count_ones:
            ones = '1' * count_ones
            big_odd_num.appendleft(ones)
        
        
        return "".join(big_odd_num)

