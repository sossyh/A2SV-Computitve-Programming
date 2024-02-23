class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        arr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = set()

        for word in words:
            word_arr = ""

            for char in word:
                idx = ord(char) - 97
                word_arr += arr[idx]
            
            ans.add(word_arr)
        
        return len(ans)