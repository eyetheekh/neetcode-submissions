class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp:dict = {}
        for i in strs:
            
            key = tuple(sorted(i))
            if key in mapp:
                mapp[key].append(i)
            else:
                mapp[key] = [i,]

        return list(mapp.values())