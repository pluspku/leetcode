class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        a = sorted(range(len(height)), key = lambda i: height[i], reverse = True)
        lb = {}
        rb = {}
        ulb = 0
        urb = len(height)
        for p in a:
            for i in xrange(p, urb):
                rb[i] = height[p]
            urb = min(p, urb)
            for i in xrange(ulb, p):
                lb[i] = height[p]
            ulb = max(p, ulb)
        tot = 0
        for i in xrange(len(height)):
            vol = max(0, min(lb.get(i, 0), rb.get(i, 0)) - height[i])
            tot += vol
        return tot

            
        



sample = [0,1,0,2,1,0,1,3,2,1,2,1]
expected = 6

print Solution().trap(sample)
