class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashMapS = {}
        hashMapT = {}

        for i in range(len(s)):
            hashMapS[s[i]] = hashMapS.get(s[i], 0) + 1
        
        for i in range(len(t)):
            hashMapT[t[i]] = hashMapT.get(t[i], 0) + 1

        if hashMapS == hashMapT:
            return True
        else:
            return False
        