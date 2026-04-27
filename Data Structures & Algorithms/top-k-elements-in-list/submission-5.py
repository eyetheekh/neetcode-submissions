class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}
        for num in nums:
            mapp[num] = mapp.get(num, 0) + 1

        bucket = [ [] for _ in range(len(nums) + 1)]

        for num, count in mapp.items():
            bucket[count].append(num)

        res = []
        for collection in range(len(bucket) -1, 0 , -1):
            for i in bucket[collection]:
                res.append(i)
                if len(res) == k:
                    return res
                
                