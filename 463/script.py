class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        tot = 0
        N = len(grid)
        for i, row in enumerate(grid):
            M = len(row)
            for j, cell in enumerate(row):
                if cell:
                    if i == 0 or not grid[i-1][j]:
                        tot += 1
                    if i == N-1 or not grid[i+1][j]:
                        tot += 1
                    if j == 0 or not grid[i][j-1]:
                        tot += 1
                    if j == M-1 or not grid[i][j+1]:
                        tot += 1
        return tot

                

grid = [[0,1,0,0],
         [1,1,1,0],
          [0,1,0,0],
           [1,1,0,0]]
print Solution().islandPerimeter(grid)
