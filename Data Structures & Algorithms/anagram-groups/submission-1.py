class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mapp:dict = {} # global collection map
        
        for i in strs:
            
            c_arr = [0] *26 # array for storing index of charectors in i
            for c in i:
                c_arr[ord(c) - ord("a")] += 1 # ord(c) - ord("a") always gives a number btw 0,25 which corresponds to index of the charector in alphabetical order
            
            key = tuple(c_arr) # convert to tuple to make the list hashable
            if key in mapp:
                mapp[key].append(i)
            else:
                mapp[key] = [i,]

        return list(mapp.values())