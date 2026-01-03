class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def all_pal(lis):
            for word in lis:
                left , right = 0 , len(word)-1
                while left < right:
                    if word[left]!=word[right]:
                        return False
                    left +=1
                    right -=1
            return True
        def backtrack(index , temp , curr_ans):
            if index == len(s):
                if temp:
                    curr_ans.append(temp)
                if all_pal(curr_ans):
                    ans.append(curr_ans.copy())
                if temp:
                    curr_ans.pop()
                return
            if len(temp):
                backtrack(index + 1 , temp + s[index] , curr_ans)
                curr_ans.append(temp)
                backtrack(index +1 , s[index] , curr_ans)
                curr_ans.pop()
            else:
                backtrack(index+1 , s[index] , curr_ans)
        backtrack(0 , '' , [])
        return ans