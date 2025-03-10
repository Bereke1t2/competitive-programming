class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def howmuch(num):
            non_v = defaultdict(int)
            v = 0
            left = 0
            count = 0
            for right in range(len(word)):
                if word[right] in 'aioue':
                    non_v[word[right]] +=1
                else:
                    v +=1
                while len(non_v)==5 and v>=num:
                    count +=len(word) - right
                    if word[left] in 'aioue':
                        non_v[word[left]] -=1
                        if not  non_v[word[left]]:
                            del  non_v[word[left]]
                    else:
                        v -=1
                    left +=1
            return count
        return howmuch(k) - howmuch(k+1)
        
