class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        input = '%s\n' % input
        prefix = {0: 0}
        s = -1
        level = 0
        L = 0
        ML = 0
        for i, c in enumerate(input):
            if c == '\n':
                L = prefix[level] + (i-s)
                prefix[level+1] = L
                fname = input[s+1:i]
                if '.' in fname:
                    ML = max(L - 1, ML)
                level = 0
                s = i
            elif c == '\t':
                level += 1
                s = i
        return ML

        

fn = Solution().lengthLongestPath
sample = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
assert fn(sample) == 32
sample = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.txt"
assert fn(sample) == 20
sample = "dir\n    file.txt"
assert fn(sample) == 12
sample = 'a.txt'
assert fn(sample) == 5
