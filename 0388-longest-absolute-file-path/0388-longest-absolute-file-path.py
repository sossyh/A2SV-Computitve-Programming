import re
class Solution:
    def agrigate(self, path):
        extpath = []
        pattern = r'^(\t*)([a-zA-Z0-9\s]+(?:\.[a-zA-Z0-9\s]+)*)$'
                    # ^(\t*)([a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*)$

        patternd = r'^(\t*)([a-zA-Z0-9\s]+)$'

        
        for string in path:
            match = re.match(pattern, string)
            dmatch = re.match(patternd, string)
            if match:
                indentation_level = len(match.group(1))
                a = match.group(2)
                extpath.append((a, indentation_level))
            if dmatch:
                i = len(dmatch.group(1))
                a = dmatch.group(2)
                extpath.append((a, i))
                
                
        return extpath
    
    def lengthLongestPath(self, input: str) -> int:
        path = input.split("\n")
        path = self.agrigate(path)
        filenamepattern = r'[a-zA-Z0-9\s]+\.[a-zA-Z0-9\s]+'
        stack = []
        dirlen = 0
        currdir = 0
        
        for item in path:
            while stack and stack[-1][1] >= item[1]:
                a = stack.pop()
                currdir -= len(a[0])
            
            stack.append(item)
            currdir += len(item[0])
            
            
            if re.match(filenamepattern, item[0]):
                dirlen = max(dirlen, (currdir+len(stack)-1))
                
        
        return dirlen
                