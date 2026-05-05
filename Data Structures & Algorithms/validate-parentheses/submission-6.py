class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:  # always need the length of sting to be even to get pairs
            return False

        stack = []
        pairs = {")": "(", "}": "{", "]": "["}

        for i in s:
            if i not in pairs:  # ie its an opening bracket
                stack.append(i)  # add openings to stack
            else:  # all closing brackets
                if not stack:
                    return False

                if stack[-1] != pairs[i]:  # check if last item in stack equals with the current string's opening
                    return False
                
                else: # pop when the brackets are same
                    stack.pop()  

        return len(stack) == 0
