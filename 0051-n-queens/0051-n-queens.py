class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        under_attack_r = set()
        under_attack_c = set()
        under_attack_d1 = set()
        under_attack_d2 = set()

        def dfs(r,curr_ans):
            if r==n:
                print(r)
                ans.append([part for part in curr_ans])
                return 
            
            for c in range(n):
                if c not in  under_attack_c and r not in under_attack_r and r+c not in under_attack_d1 and r-c not in under_attack_d2:
                    under_attack_c.add(c)
                    under_attack_r.add(r)
                    under_attack_d1.add(r+c)
                    under_attack_d2.add(r-c)
                    curr_ans.append(''.join(['Q' if i==c else '.' for i in range(n)]))
                    dfs(r+1 , curr_ans)
                    curr_ans.pop()
                    under_attack_c.discard(c)
                    under_attack_r.discard(r)
                    under_attack_d1.discard(r+c)
                    under_attack_d2.discard(r-c)
        dfs(0,[])
        return ans
                