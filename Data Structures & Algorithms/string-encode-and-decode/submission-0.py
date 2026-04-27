class Solution:

    def encode(self, strs: List[str]) -> str:
        separator = ""
        joined = ""

        for s in strs:
            joined += f"{s}{separator}"
        print(joined)
        return joined

            


    def decode(self, s: str) -> List[str]:
        strs = s.split("")
        print(strs)
        res = []
        for i in strs[:-1]:
            res.append(i)
        return res





