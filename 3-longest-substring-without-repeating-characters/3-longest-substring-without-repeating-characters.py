class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        stor={}
        lis=[]
        
        start=0
        for i in s:
            if i not in stor:
                stor[i]=-1
                
        lis.append(0)
        for idx, ele in enumerate(s):
            if idx==0:
                lis[-1]+=1
                stor[ele]=0
                continue
            if stor[ele]< start:
                stor[ele]=idx
                lis[-1]+=1
            else:
                start=stor[ele]+1
                stor[ele]=idx
                lis.append(idx -(start)+1)
        
        lis.sort()
        return lis[-1]
                
        