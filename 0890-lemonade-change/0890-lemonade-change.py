class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)
        for bill in bills:
            if bill == 5:
                change[bill] +=1
            elif bill == 10:
                if change[5]:
                    change[5]-=1
                    change[bill] +=1
                else:
                    return False
            else:
                if change[10]:
                    change[10] -=1
                    bill -=10
                while change[5] and bill!=5:
                    change[5] -=1
                    bill -=5
                if bill!=5:
                    return False
        return True
        