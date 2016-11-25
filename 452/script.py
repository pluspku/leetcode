class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points = sorted(points)
        r = points[0][0] - 1
        cnt = 0
        for s, e in points:
            if s <= r:
                if e < r:
                    r = e
            else:
                cnt += 1
                r = e
        return cnt

print Solution().findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]])



