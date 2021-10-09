class Solution:
        
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtracking(S, lcount, rcount):
            nonlocal n
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            
            if lcount < n:
                S.append('(')
                backtracking(S, lcount + 1, rcount)
                S.pop()
                
            if rcount < lcount:
                S.append(')')
                backtracking(S, lcount, rcount + 1)
                S.pop()
        
        backtracking([], 0, 0)
        return ans