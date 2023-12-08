class Solution:
    def generateRow(self, curr_row):
        if curr_row == 1:
            self.pascal_triange.append([1])
            return [1]
        
        row = [1]
        prev_row = self.generateRow(curr_row - 1)

        for i in range(len(prev_row) - 1):
            row.append(prev_row[i] + prev_row[i + 1])
        
        row.append(1)

        self.pascal_triange.append(row)

        return row



    def generate(self, numRows: int) -> List[List[int]]:
        # will recursion 
        # state - the curr row
        # recurrence relation - the curr row is the sum of the elements frpm the above row which are directly above it
        # two basecases - 1. when n == 1 -- return [1]

        self.pascal_triange = []

        self.generateRow(numRows)

        return self.pascal_triange 