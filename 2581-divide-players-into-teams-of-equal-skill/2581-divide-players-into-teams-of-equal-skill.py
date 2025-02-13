class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemo = 0
        left , right = 0, len(skill)-1
        while left < right:
            if skill[left] + skill[right]!=skill[0] + skill[-1]:
                return -1
            chemo +=skill[left] * skill[right]
            left +=1
            right -=1
        return chemo
        