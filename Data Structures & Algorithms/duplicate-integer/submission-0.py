class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique : set = set()
        for i in nums:
            if i not in unique:
                unique.add(i)
                continue
            return True
        return False
            
        