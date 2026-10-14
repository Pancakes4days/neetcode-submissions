class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #instantiate left, maxfrequent
        l = 0
        maxf = 0
        longest = 0
        
        #instantiate the hashmap to count how many times
        #we see a letter in a substring
        count = defaultdict(int)

        #enumerate through s
        for r, val in enumerate(s):

            #add the val we are on to hashmap adding one instanc of it
            count[val] += 1
            #check if there is a larger count of most frequent letter
            maxf = max(maxf, count[val])
            #while: window size - most frequent number > k
            #meaning you would need to fill the least freq num with k
            #and theres no point in that since we want to fill the MOST
            #frequent per subarray
            while (r - l + 1) - maxf > k:

                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest
            
            
            
        