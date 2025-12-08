class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_set = set()
        res = 0

        for c in s:
            if c in char_set:
                res += 2
                char_set.remove(c)
            else:
                char_set.add(c)
        
        # If any character remains, we have at least one unmatched
        # character to make the center of an odd length palindrome.
        if char_set:
            res += 1
        
        return res        
