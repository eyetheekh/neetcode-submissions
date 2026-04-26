class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for idx, num in enumerate(nums):
            x = target - num
            if x in mapp:
                return [mapp[x], idx]
            else:
                mapp[num] = idx