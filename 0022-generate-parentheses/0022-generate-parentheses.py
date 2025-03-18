class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def back(p,sub_ans,opend,closed):
            nonlocal ans
            sub_ans +=p
            if 2*n ==len(sub_ans):
                ans.append(sub_ans)
                return
            if opend<n:
                if opend>closed:
                    back(')',sub_ans,opend,closed+1)
                    back('(',sub_ans,opend+1,closed)
                else:
                    back('(',sub_ans,opend+1,closed)
            else:
                back(')',sub_ans,opend,closed+1)
        back('','',0,0)           
        return ans
        