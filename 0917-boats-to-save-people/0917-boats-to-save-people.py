class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        left ,right = 0, len(people)-1
        while left <= right:
            total_weight = people[left] + people[right]
            if total_weight<=limit:
                left +=1
            right -=1
            boats +=1
        return boats
        