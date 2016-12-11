class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.N = len(nums)
        self.nums = nums[:]

        M = 64

        self.masks = []
        for i in xrange(M):
            self.masks.append((2**(M-i) - 1) * 2**i)

        self.M = M

        self.partial = [0] * (self.N+1)

        cumsum = [0] * (self.N + 1)
        for i in xrange(self.N):
            cumsum[i+1] = cumsum[i] + nums[i]

        ms = [2**i for i in xrange(M)]
        for i in xrange(self.N):
            j = i + 1
            for m in ms:
                if j & m:
                    self.partial[j] = cumsum[j] - cumsum[j - m]
                    break

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        delta = val - self.nums[i]
        self.nums[i] = val

        i += 1

        i0 = i
        k0 = 0
        updates = []
        while i % 2 == 0:
            k0 += 1
            i /= 2

        updates.append(i0)
        for k in xrange(k0, self.M - 1):
            if (i0 & (2**k) == 0):
                j = (i0 & self.masks[k + 1]) + 2**(k)
                if j <= self.N:
                    updates.append(j)

        for j in updates:
            self.partial[j] += delta

    def cumsum(self, n):
        s = 0
        i = 0
        n0 = n
        while n:
            if n % 2:
                s += self.partial[self.masks[i] & n0]
            i += 1
            n = n / 2
        return s

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.cumsum(j+1) - self.cumsum(i)

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(1, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)

if __name__ == '__main__':
    #N = 100000
    #print NumArray(range(N)).sumRange(0, N-1)
    n = NumArray([1,3,5])
    print n.sumRange(0, 2)
    n.update(1, 2)
    print n.sumRange(0, 2)
