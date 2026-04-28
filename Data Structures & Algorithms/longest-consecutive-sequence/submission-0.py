from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        longest = 0
        for i in nums:
            if i -1 in hset:
                continue
            length = 1
            while i+length in hset:
                length +=1
            longest = max(longest, length)

        
        return longest
             