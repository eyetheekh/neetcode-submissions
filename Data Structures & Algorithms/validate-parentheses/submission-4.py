class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        arr = []
        closings = {")": "(", "}": "{", "]": "["}
        for b in s:
            if not b in closings:
                arr.append(b)
            else:
                if not arr:
                    return False
                
                popped = arr.pop()
                if popped != closings[b]:
                    return False
        
        return len(arr) == 0 
