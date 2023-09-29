# class TrieNode:
#     def __init__(self) -> None:
#         self.children = {}
#         self.end = False
        
# class Trie:
#     def __init__(self) -> None:
#         self.root = TrieNode()
    
#     def insert(self, lst):
#         curr = self.root
#         comparator = self.root
#         total = ""
        
#         if not self.root.children:
#             for i in lst:
#                 if i not in curr.children:
#                     curr.children[i] = TrieNode()
#                 curr = curr.children[i]
#             return 0
#         else:
#             for i in lst:
#                 if i not in curr.children:
#                     curr.children[i] = TrieNode()
                    
#                 if i == 1:  
#                     if 0 in comparator.children:
#                         total += str(1)
#                         comparator = comparator.children[0]
#                     else:
#                         total += str(0)
#                         # if 1 not in comparator.children:
#                         #     comparator.children[1] = TrieNode()
#                         comparator = comparator.children[1]
#                 else:
#                     if 1 in comparator.children:
#                         total += str(1)
#                         comparator = comparator.children[1]
#                     else:
#                         total += str(0)
#                         if 0 not in comparator.children:
#                             comparator.children[0] = TrieNode()
#                         comparator = comparator.children[0]
                
#                 curr = curr.children[i]
        
#         return int(total, 2)

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        a = max(nums)
        l = len(bin(a)) - 2
        maxxor = 0
        
        for i in range(l-1, -1, -1):
            prefix = {(num >> i) for num in nums}
            
            currxor = maxxor | (1 << i)
            currxor >>= i
         
            for j in prefix:
                if (j ^ currxor) in prefix:
                    maxxor = currxor << i
                    break
                    
    
        
        return maxxor
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        