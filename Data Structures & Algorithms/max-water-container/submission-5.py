class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = float("-inf")
        while l < r:
            length = r - l
            height = min(heights[l], heights[r])

            if (length * height) > area:
                area = length * height

            if heights[l] < heights[r]:
                l += 1

            elif heights[l] > heights[r]:
                r -= 1

            else:
                r -= 1

        return area
