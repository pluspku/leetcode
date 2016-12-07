class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        mapping = {}
        for i, (src, dst) in enumerate(tickets):
            mapping.setdefault(src, []).append(i)

        for k in mapping:
            mapping[k].sort(key = lambda i: tickets[i][1])
        def dfs(stack):
            if len(stack) == len(tickets):
                return stack[:]
            src = tickets[stack[-1]][1]
            for i in mapping.get(src, []):
                if i in stack:
                    continue
                stack.append(i)
                res = dfs(stack)
                if res:
                    return res
                stack.pop()
            return None

        for i in mapping['JFK']:
            res = dfs([i])
            if res:
                airports = ['JFK'] + [tickets[i][1] for i in res]
                return airports
        return None


        



tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
#tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

print Solution().findItinerary(tickets)
