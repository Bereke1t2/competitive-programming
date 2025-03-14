class Solution:
    def help(self,r,c,l,dp):
        if r<=0 or c<=0:
            return [0,dp]
        if r ==1 or c == 1 or c==l:
            return [1,dp]
        if not (r,c) in dp.keys():
            dp[(r,c)]=self.help(r-1,c-1,l-1,dp)[0] + self.help(r-1,c,l-1,dp)[0]
        return [dp[(r,c)],dp]
    def getRow(self, rowIndex: int) -> List[int]:
        dp={}
        ans =[]
        for num in range(rowIndex+1):
            value , dp = self.help(rowIndex+1,num+1,rowIndex+1,dp)
            ans.append(value)


        return  ans