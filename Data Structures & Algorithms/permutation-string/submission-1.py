class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        k = len(s1)

        #length check
        if k > len(s2):
            return False
        
        need = Counter(s1)
        window = Counter()

        for r in range(len(s2)):
            window[s2[r]] += 1

            #window now has k + 1 letters, so remove the
            # leftmost one (s2[r - k]) to bring it back to k
            if r >= k:
                window[s2[r - k]] -= 1

            #if window is correct size AND window equals the      
            #anagram we need return True
            if r >= k - 1 and window == need:
                return True

        return False
            




        