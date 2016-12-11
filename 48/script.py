class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if not n:
            return
        for i in xrange(n/2):
            for j in xrange((n+1)/2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = tmp


N = 5
import numpy
m = numpy.matrix(range(N*N)).reshape((N, N))

a = m.tolist()
Solution().rotate(a)
#print m
b = numpy.matrix(a).reshape((N, N))
print numpy.all(b == numpy.rot90(m, 3))
