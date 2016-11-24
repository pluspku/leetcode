# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

a = 6
def guess(x):
    return cmp(a, x) 


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while True:
            mid = (l + r) / 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res > 0:
                l = mid + 1
            else:
                r = mid - 1


while True:
    n, a = input()
    print Solution().guessNumber(n)
