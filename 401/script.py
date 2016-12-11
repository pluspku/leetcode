class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ret = []
        masks = [2**i for i in xrange(11)] 
        for i in xrange(1024):
            s = sum(bool(m & i) for m in masks)
            if s == num:
                h = i / 64
                if h > 11:
                    continue
                m = i % 64
                if m >= 60:
                    continue
                ret.append('%d:%02d' % (h, m))
        return ret


print Solution().readBinaryWatch(3)
