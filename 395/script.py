class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0
        from collections import Counter
        cnt = Counter(s)
        breaks = []
        for c in cnt:
            if cnt[c] < k:
                breaks.append(c)
                s = s.replace(c, ' ')

        if not breaks:
            return len(s)

        m = 0
        for subs in s.split(' '):
            m = max(m, self.longestSubstring(subs, k))

        return m

fn = Solution().longestSubstring

print fn('ababbc', 2)



