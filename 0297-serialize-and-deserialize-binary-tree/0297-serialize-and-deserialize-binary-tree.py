# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.seri = []
        
        def traverse(root):
            if not root:
                self.seri.append("null")
                self.seri.append("+")
                return
            
            self.seri.append(str(root.val))
            self.seri.append("+")
            traverse(root.left)
            traverse(root.right)
        
        traverse(root)
        
        return "".join(self.seri)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split("+")
        
        def construct(idx):
            if data[idx] == "null":
                return [idx, None]
            
            root = TreeNode(int(data[idx]))
            
            left = construct(idx + 1)
            root.left = left[1]
            
            right_idx = left[0] + 1
            right = construct(right_idx)
            
            root.right = right[1]
            
            value = max(left[0], right[0])
            
            return [value, root]
        
        ans = construct(0)
            
            
        
        return ans[1]
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))