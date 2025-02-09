class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter  = Counter(answers)
        count = 0
        for key in counter:
            count +=(key+1)*(ceil(counter[key]/(key+1)))
        return count 
            

        