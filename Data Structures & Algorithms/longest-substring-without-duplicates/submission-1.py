class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub = 0
        
        for i in range(len(s)):
            char_set = set()
            for j in range(i, len(s)):
                if s[j] not in char_set:
                    char_set.add(s[j])
                else:
                    break
            
            max_sub = max(max_sub, len(char_set))
            
        return max_sub
