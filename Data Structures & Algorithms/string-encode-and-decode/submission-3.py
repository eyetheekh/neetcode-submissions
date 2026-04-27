class Solution:
    def encode(self, strs: List[str]) -> str:
        separator = "#"
        joined = ""

        for s in strs:
            joined += f"{len(s)}{separator}{s}"
        
        print('joind', joined)
        return joined


    def decode(self, s: str) -> List[str]:
        separator = "#"
        res = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != separator:
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res












