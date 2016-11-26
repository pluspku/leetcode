class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        cnt = Counter(s)
        res = {}
        #zero
        res[0] = cnt['z']
        cnt['e'] -= cnt['z']
        cnt['r'] -= cnt['z']
        cnt['o'] -= cnt['z']
        cnt['z'] = 0

        #two
        res[2] = cnt['w']
        cnt['t'] -= cnt['w']
        cnt['o'] -= cnt['w']
        cnt['w'] = 0

        #six
        res[6] = cnt['x']
        cnt['s'] -= cnt['x']
        cnt['i'] -= cnt['x']
        cnt['x'] = 0

        #eight
        res[8] = cnt['g']
        cnt['e'] -= cnt['g']
        cnt['i'] -= cnt['g']
        cnt['h'] -= cnt['g']
        cnt['t'] -= cnt['g']
        cnt['g'] = 0

        #four
        res[4] = cnt['u']
        cnt['f'] -= cnt['u']
        cnt['o'] -= cnt['u']
        cnt['r'] -= cnt['u']
        cnt['u'] = 0

        #five
        res[5] = cnt['f']
        cnt['i'] -= cnt['f']
        cnt['v'] -= cnt['f']
        cnt['e'] -= cnt['f']
        cnt['f'] = 0

        #seven
        res[7] = cnt['v']
        cnt['s'] -= cnt['v']
        cnt['e'] -= 2 * cnt['v']
        cnt['n'] -= cnt['v']
        cnt['v'] = 0

        #one
        res[1] = cnt['o']
        cnt['n'] -= cnt['o']
        cnt['e'] -= cnt['o']
        cnt['o'] = 0

        #nine
        res[9] = cnt['i']
        cnt['n'] -= 2 * cnt['i']
        cnt['e'] -= cnt['i']
        cnt['i'] = 0

        #three
        res[3] = cnt['r']
        cnt['t'] -= cnt['r']
        cnt['h'] -= cnt['r']
        cnt['e'] -= 2 * cnt['r']
        cnt['r'] = 0

        return ''.join(''.join([str(i)] * res[i]) for i in range(10))

print Solution().originalDigits('fviefuro')
