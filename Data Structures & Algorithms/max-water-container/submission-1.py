class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        volume = float("-inf")
        while l < r:
            length = r - l
            width = min(heights[l], heights[r])
            if (length * width ) > volume:
                volume = length * width
                print(volume)
            if heights[l] < heights[r]:
                l+=1
                continue
            elif heights[l] > heights[r]:
                r-=1
                continue
            else:
                l+=1
                # r-=1
        return volume