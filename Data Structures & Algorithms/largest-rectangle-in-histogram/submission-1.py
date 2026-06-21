class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        
        n=len(heights)
        stack=[]
        max_area=0

        for i in range(n):
            while stack and heights[stack[-1]]>heights[i]:
                h=heights[stack.pop()]

                if stack:
                    width=i-stack[-1]-1

                else:
                    width=i

                max_area=max(max_area,h*width)

            stack.append(i)

        return max_area

        