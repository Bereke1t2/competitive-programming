class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations) 
        count  =[0]*(len(citations)+1)
        for c in citations:
            if c>=N:
                count[N] +=1
            else:
                count[c] +=1
        for i in range(N-1,-1,-1):
            count[i] +=count[i+1]
            if count[i+1] >=i+1 :
                return i+1
        return 0
        

        