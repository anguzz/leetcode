#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

'''example
input digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
'''
PHONE_BUTTONS = {
    "0": [],
    "1": [],
    "2":["a","b","c"],
    "3":["d","e","f"],
    "4":["g","h","i"],
    "5":["j","k","l"],
    "6":["m","n","o"],
    "7":["p","q","r","s"],
    "8":["t","u","v"],
    "9":["w","x","y","z"],
}
class Solution(object):    
    def letterCombinations(self, digits):
        if len(digits)==0:return [] #base case
        
        letter_combos=[]
        def combineLetters(prevString, digits):
            if len(digits)==0: 
                letter_combos.append(prevString)
                return None
            
            for letter in PHONE_BUTTONS[digits[0]]:
                combineLetters(prevString+letter, digits[1:])
            
        combineLetters("",digits)
        return letter_combos

       
