class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        under_attack_c = set()
        under_attack_d1 = set()
        under_attack_d2 = set()

        def dfs(r):
            if r==n:
                self.count +=1
                return 
            for c in range(n):
                if c not in  under_attack_c and r+c not in under_attack_d1 and r-c not in under_attack_d2:
                    under_attack_c.add(c)
                    under_attack_d1.add(r+c)
                    under_attack_d2.add(r-c)
                    dfs(r+1)
                    under_attack_c.discard(c)
                    under_attack_d1.discard(r+c)
                    under_attack_d2.discard(r-c)
        dfs(0)
        return self.count
                