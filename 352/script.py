# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self):
        return '<%s,%s>' % (self.start, self.end)

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lpoints = {}
        self.rpoints = {}
        self.used = {}
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if val in self.used:
            return
        self.used[val] = True
        intv = Interval(val, val)
        if val in self.lpoints:
            intv.end = self.lpoints[val].end
            del self.lpoints[val]
        if val in self.rpoints:
            intv.start = self.rpoints[val].start
            del self.rpoints[val]

        self.lpoints[intv.start-1] = intv
        self.rpoints[intv.end+1] = intv
       

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return sorted(self.lpoints.values(), key = lambda x: x.start)


# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
#seq = [1,3,7,2,6]
seq = [6,6,0,4,8,7,6,4,7,5]
for x in seq:
    obj.addNum(x)
    print obj.getIntervals()
