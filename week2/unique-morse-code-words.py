class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        result = set()
        for word in words:
            converted = self.generate_converted_word(word)
            result.add(converted)
        return len(result)
                
            

    def generate_converted_word(self, word):
        converted_letters = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = ""
        for letter in word:
            res = res + converted_letters[ord(letter) - ord('a')]
        return res
            