"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ID = {}
        for e in employees:
            ID[e.id] = e
        
        def total(id):
            e = ID[id]
            Sum = e.importance
            for sub_e in e.subordinates:
                Sum +=total(sub_e)
            return Sum
        return total(id)
        