class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        for letter in s:
            if s.count(letter) != t.count(letter):
                return False       
        return True