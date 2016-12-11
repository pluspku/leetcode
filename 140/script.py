class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        fn = {-1: [[]]}
        for i in xrange(len(s)):
            fn[i] = []
            for w in wordDict:
                if s[(i-len(w))+1:i+1] == w and fn[i-len(w)]:
                    fn[i].append(i - len(w))

        ret = []
        def dfs(stack, i):
            if i == -1:
                ret.append(' '.join(stack[::-1]))
            else:
                for u in fn[i]:
                    stack.append(s[u+1:i+1])
                    dfs(stack, u)
                    stack.pop()

        dfs([], len(s)-1)
        return ret


#print Solution().wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"])

fn = Solution().wordBreak
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wd = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print fn(s, wd)
