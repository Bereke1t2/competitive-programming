class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        d = Counter(letters)

        def backtrack(i,scores):
            nonlocal d, score , words
            if i>=len(words):

                return scores
            first = backtrack(i+1,scores)
            word = words[i]
            
            for j in range(len(word)):
                l = word[j]
                d[l] -=1
                scores +=score[ord(l) - ord('a')]
                if d[l]<0:
                    while j>-1:
                        l = word[j]
                        d[l] +=1
                        scores -=score[ord(l) - ord('a')]
                        j-=1
                    return first
            second = backtrack(i+1,scores)
            j = len(word)-1
            while j>-1:
                l = word[j]
                d[l] +=1
                scores -=score[ord(l) - ord('a')]
                j-=1
            return max(first , second)
        return backtrack(0,0)