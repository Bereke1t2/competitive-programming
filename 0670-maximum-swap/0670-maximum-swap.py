class Solution:
    def maximumSwap(self, num: int) -> int:
        res = [int(l) for l in str(num)] 
        for i in range(len(res)):
            max_= res[i]
            index = i
            print(i)
            for j in range(i+1,len(res)):
                if max_ <=res[j]:
                    index = j
                    max_ = res[j]
            if res[i]!=res[index]:
                res[i] , res[index] = res[index] , res[i]
                break
        return int(''.join([str(l) for l in res]))
        

