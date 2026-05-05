class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        max_sub = 0
        
        for r in range(len(s)):
            # If we hit a duplicate, shrink the window from the left
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            # Add the current character and update the record
            char_set.add(s[r])
            max_sub = max(max_sub, r - l + 1)
            
        return max_sub
