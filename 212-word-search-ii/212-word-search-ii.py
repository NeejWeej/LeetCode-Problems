class Solution: 
    def makeTrie(self, words):
        self.root = {}
        for word in words:
            cur = self.root
            for c in word:
                if c in cur:
                    nextt = cur.get(c)
                else:
                    nextt = {}
                    cur[c] = nextt
                    nextt['^'] = cur
                cur = nextt
            cur['+'] = True
        return
    
    def remove(self, word, node):
        cur = node
        del cur['+']
        letter_idx = len(word) - 1
        while len(cur) == 1:
            p = cur.get('^')
            if not p:
                return
            del p[word[letter_idx]]
            letter_idx -= 1
            del cur
            cur = p
        return
                
                
    def search(self, r, c, cur, path, neighs, board):
        self.visited.add((r,c))
        if '+' in cur:
            new_word = "".join(path)
            self.ans.add(new_word)
            self.remove(new_word, cur)
        if len(self.root) == 0:
            return
        for dx, dy in neighs:
            if not (0 <= r + dx < len(board) and 0<= c + dy < len(board[0])):
                continue
            if (r + dx, c + dy) in self.visited:
                continue
            next_letter = board[r + dx][c + dy]
            if next_letter not in cur:
                continue
            new_cur = cur.get(next_letter)
            path.append(next_letter)
            self.search(r + dx, c + dy, new_cur, path, neighs, board)
        self.visited.discard((r, c))
        path.pop()
        return
             
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.makeTrie(words)
        self.ans = set()
        neighs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m = len(board)
        n = len(board[0])
        self.visited = set()
        for r in range(m):
            for c in range(n):
                letter = board[r][c]
                if letter not in self.root:
                    continue
                node = self.root.get(letter)
                self.search(r, c, node, [letter], neighs, board)
                if len(self.root) == 0:
                    return self.ans
        return list(self.ans)
                