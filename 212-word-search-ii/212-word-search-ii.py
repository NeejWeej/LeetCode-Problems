class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        m = len(board)
        n = len(board[0])
        for word in words:
            cur = trie
            for c in word:
                cur[c] = cur.get(c, {})
                old = cur
                cur = cur.get(c)
                cur['parent'] = old
                cur['val'] = c
            cur['#'] = word
                
        direc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.ans = []
        # print(trie)
        def delete(node):
            while len(node) == 2 and node is not trie:
                char = node.get('val')
                node = node.get('parent')
                del node[char]
            return node
                
        
        def search(curChar, r, c):
            old = board[r][c]
            board[r][c] = '$'
            node = curChar
            if '#' in curChar:
                self.ans.append(curChar.get('#'))
                del curChar['#']
                node = delete(curChar)
            
            if node == curChar:
                for dx, dy in direc:
                    if 0<= r+dx < m and 0<=c+dy<n:
                        val = board[r + dx][c + dy]
                        if val in curChar:
                            search(curChar.get(val), r+dx, c+dy)
            board[r][c] = old
        
        for i in range(m):
            for j in range(n):
                char = board[i][j]
                if char in trie:
                    search(trie.get(char), i, j)
        
        return self.ans
        
        