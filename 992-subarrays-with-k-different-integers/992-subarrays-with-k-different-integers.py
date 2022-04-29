class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        window=[0,0]
        uniq_count=0
        
        stor={}
        
        for i in A:
            stor[i]=0
        
        m=0
        j=0
        while uniq_count<K:
            stor[A[m]]+=1
            if stor[A[m]]==1:
                uniq_count+=1            
            if uniq_count==K:
                break
            m+=1
            if m>=len(A):
                return 0
        window[1]=m
        while window[0]<len(A):
            v=window[1]
            j+=1
            if window[1]<len(A)-1:
                window[1]+=1
                while stor.get(A[window[1]])>0:
                    j+=1
                    if window[1]==len(A)-1:
                        break
                    window[1]+=1
            window[1]=v
            stor[A[window[0]]]-=1
            if stor[A[window[0]]]==0:
                if window[1]==len(A)-1:
                        return j
                window[1]+=1
                while stor.get(A[window[1]])>0:
                    stor[A[window[1]]]+=1
                    if window[1]==len(A)-1:
                        return j
                    window[1]+=1
                stor[A[window[1]]]+=1
            window[0]+=1
                
        return j
                