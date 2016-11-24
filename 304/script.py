class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        ps = []
        for i, row in enumerate(matrix):
            ps.append([])
            for j, v in enumerate(row):
                a = ps[i-1][j-1] if i > 0 and j > 0 else 0
                b = ps[i-1][j] if i > 0 else 0
                c = ps[i][j-1] if j > 0 else 0
                ps[i].append(b+c+v-a)
        self.ps = ps

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        v = self.ps[row2][col2]
        a = self.ps[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        b = self.ps[row1-1][col2] if row1 > 0 else 0
        c = self.ps[row2][col1-1] if col1 > 0 else 0
        return v - b - c + a
        


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)


matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

numMatrix = NumMatrix(matrix)
print numMatrix.ps
print numMatrix.sumRegion(2, 1, 4, 3)
print numMatrix.sumRegion(1, 1, 2, 2)
print numMatrix.sumRegion(1, 2, 2, 4)
