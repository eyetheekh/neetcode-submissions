class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = float("-inf")
        while l < r:
            length = r - l
            height = min(heights[l], heights[r])
            if (length * height ) > area:
                area = length * height
            if heights[l] < heights[r]:
                l+=1
                continue
            elif heights[l] > heights[r]:
                r-=1
                continue
            else:
                l+=1

        return area