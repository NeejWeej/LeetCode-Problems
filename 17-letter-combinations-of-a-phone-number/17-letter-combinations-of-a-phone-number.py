class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        vals = [[]]
        start = ord('a')
        mappings = {}
        for i in range(2, 10):
            dig = str(i)
            alphabetVal = []
            for _ in range(3):
                alphabetVal.append(chr(start))
                start += 1
            if i in [7, 9]:
                alphabetVal.append(chr(start))
                start += 1
            mappings[dig] = alphabetVal
        
        for d in digits:
            newV = []
            for char in mappings.get(d):
                for v in vals:
                    newV.append(v + [char])
            vals = newV
            
        return ["".join(v) for v in vals]
            
                