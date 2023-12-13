class MagicDictionary:

    def __init__(self):
        self.dict = None

    def buildDict(self, dictionary: List[str]) -> None:
        self.dict = dictionary
        

    def search(self, searchWord: str) -> bool:

        for word in self.dict:
            count_diff = 0
            if len(word) == len(searchWord):
                for pointer in range(len(word)):
                    if word[pointer] != searchWord[pointer]:
                        count_diff += 1

                if count_diff == 1: 
                    return True
        
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)

""""
problem: seaching a word with only letter one letter difference from one the dictionary

Solutiom:
         1. inintialize the dictionary
         2. assign the given diction #1
         3. iterate ovet the dictionary and check for a word which has only one letter diffrence
                        - if get - return true else False

complexty analysis
N - len(dictionary)
1. checking biuiddixt - TC: - O(1)
                      - SC: O(N)

N, M = len(dictionary), len of the longest in dictionary
2. Search - TC: O(N * M)
          - SC: O(1)

"""