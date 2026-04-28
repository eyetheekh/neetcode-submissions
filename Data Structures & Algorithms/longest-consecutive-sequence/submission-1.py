class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        longest = 0
        for num in nums:
            if num -1 in hset:
                continue
            length = 0
            while num + length in hset:
                length+=1
            longest = max(longest, length)
        
        return longest