class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(' ')
        if len(pattern) != len(words):
            return False
        mapping = {}
        for p, w in zip(pattern, words):
            if p not in mapping:
                mapping[p] = w
            elif mapping[p] != w:
                return False
        return len(mapping.values()) == len(set(mapping.values())):


print Solution().wordPattern('abba', 'dog cat cat dog')

        
