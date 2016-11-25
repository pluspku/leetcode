class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt, floor
        return int(floor(sqrt(n)))
        
