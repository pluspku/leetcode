import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.left = []
        self.right = []
        self.n = 0

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if self.n % 2:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)

        while self.left and self.right and -self.left[0] > self.right[0]:
            x = -self.left[0]
            y = self.right[0]
            heapq.heapreplace(self.left, -y)
            heapq.heapreplace(self.right, x)
        self.n += 1

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.n % 2:
            return -self.left[0]
        else:
            return (-self.left[0] + self.right[0]) / 2.0
        

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
for x in xrange(10):
    mf.addNum(x)
    print mf.findMedian()

