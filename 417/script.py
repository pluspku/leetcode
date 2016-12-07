class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        R = len(matrix)
        C = len(matrix[0])
        def search(x0, y0, outer):
            visited = set()
            q = [(x0 + outer, i) for i in xrange(0, C)] + [(j, y0 + outer) for j in xrange(0, R)]
            while q:
                x, y = q.pop()
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    x1 = x + dx
                    y1 = y + dy
                    if (x1, y1) in visited:
                        continue
                    if x1 >= 0 and y1 >= 0 and x1 < R and y1 < C:
                        if x < 0 or x >= R or y <0 or y >= C:
                            visited.add((x1, y1))
                            q.append((x1, y1))
                        elif matrix[x1][y1] >= matrix[x][y]:
                            visited.add((x1, y1))
                            q.append((x1, y1))
#                            print "(%s,%s) %s -> (%s,%s) %s" % (x1, y1, matrix[x1][y1], x, y, matrix[x][y])
            return visited


        res1 = search(0, 0, -1)
        res2 = search(R-1, C-1, 1)
        return sorted([[x, y] for x, y in (res1 & res2)])





dat = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5]]


print Solution().pacificAtlantic([[1]])
