class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        can_make = {r:True for r in supplies}
        index_r = {r:index for index , r in enumerate(recipes)}

        
        def dfs(root):
            if root in can_make:
                return can_make[root]

            if root not in index_r:
                return False

            can_make[root] = False 
            for r in ingredients[index_r[root]]:
                if not dfs(r):
                    return False
            can_make[root] = True
            return True

        return [r for r in recipes if dfs(r)]