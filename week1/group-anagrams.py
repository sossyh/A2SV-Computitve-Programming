class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # defualtdict - key - sorted letters of word
        #             - value - list which contains the anagrams
        # return by combining all the values in a list

        """
        d = {"aet" : ["eat", "tea", "ate"], "ant" : ["tan", "nat"], "abt" : ["bat"]}

        ["eat","tea","tan","ate","nat","bat"]

        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

        """

        """
        n = len(strs)
        m = max_len of the word from strs


        time_complexty = O (n) * O(mlogm) == O(n * mlogm) 10, 000 * 100 * log(100) = 10^6 * 6.9

        space_complexty = o(n)

        [""]

        """

        group_anagrams = []

        anagrams = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))

            anagrams[key].append(word)
        

        for key in anagrams:
            group_anagrams.append(anagrams[key])
        
        return group_anagrams






           

        




