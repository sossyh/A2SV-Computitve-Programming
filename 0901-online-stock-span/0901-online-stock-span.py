class StockSpanner:

    def __init__(self):
        self.stack = []
        self.curr_idx = 0
        

    def next(self, price: int) -> int:
        
        lower_bound = self.curr_idx - 1
        
        while self.stack and self.stack[-1][1] <= price:
            poped_idx, poped_value = self.stack.pop()
            lower_bound = poped_idx
        
        
        self.stack.append((lower_bound, price))
        self.curr_idx += 1
        
        return self.curr_idx - lower_bound - 1

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)