class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        print(word == word.upper())
        if word == word.upper():
            return ('true')
        elif word == word.lower():
            return ('true')
        elif word[0] == word[0].upper() and word[1:] == word[1:].lower():
            return ('true')
        
        
