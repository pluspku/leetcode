class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        R = len(board)
        C = len(board[0])
        def dfs(stack):
            if len(stack) == len(word):
                return True
            x, y = stack[-1]
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x1 = x + dx
                y1 = y + dy
                if x1 < 0 or x1 >= R or y1 < 0 or y1 >= C or (x1, y1) in stack:
                    continue
                if board[x1][y1] == word[len(stack)]:
                    stack.append((x1, y1))
                    if dfs(stack):
                        return True
                    stack.pop()
            return False


        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if board[i][j] == word[0]:
                    stack = [(i,j)]
                    if dfs(stack):
                        return True
        return False

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

fn = Solution().exist

print fn(board, "ABCCED")
print fn(board, "SEE")
print fn(board, "ABCB")
