class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        fn = {(-1, -1): True}
        for i in xrange(-1, len(s1)):
            for j in xrange(-1, len(s2)):
                if i == -1 and j == -1:
                    continue
                fn[(i, j)] =  (fn.get((i-1, j), False) and s1[i] == s3[i+j+1]) or (fn.get((i, j-1), False) and s2[j] == s3[i+j+1])
        return fn[(len(s1)-1, len(s2)-1)] == True


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print Solution().isInterleave(s1, s2, s3)
s3 = "aadbbbaccc"
print Solution().isInterleave(s1, s2, s3)
