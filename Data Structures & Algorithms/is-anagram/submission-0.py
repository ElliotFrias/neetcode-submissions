class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        conts = {}
        contt = {}
        if len(s) != len(t):
            return False

        for letter in s:
            conts[letter] = conts.get(letter, 0) + 1
        
        for letter in t:
            contt[letter] = contt.get(letter, 0) + 1

        if len(conts) != len(contt):
            return False
        
        for letter in conts:
            if conts[letter] != contt.get(letter):
                return False

        return True