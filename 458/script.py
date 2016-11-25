class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        k = minutesToTest / minutesToDie
        from math import ceil, log
        return int(ceil(log(buckets) / log(k+1)))

print Solution().poorPigs(1000, 15, 60)




            

