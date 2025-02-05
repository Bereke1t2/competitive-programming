class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        store = defaultdict(int)
        sum_index = float('inf')
        words = set()

        for index , word in enumerate(list1):
            store[word] +=index
        
        for index , word in enumerate(list2):
            if word in store:
                words.add(word)
                store[word] +=index
                sum_index = min(sum_index,store[word])

        return [word for word , sum_ind in store.items()  if sum_ind == sum_index and word in words  ]
        