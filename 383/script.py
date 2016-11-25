class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        a = sorted(ransomNote)
        b = sorted(magazine)
        j = 0
        for i, c in enumerate(a):
            if j == len(b):
                return False
            if c == b[j]:
                j += 1
            else:
                while j < len(b) and b[j] < c:
                    j += 1
                if j == len(b) or b[j] != c:
                    return False
                j += 1
        return True

print Solution().canConstruct("", "")





