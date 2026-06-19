class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1=0
        p2=len(heights)-1
        water=0

        while p1<p2:
            curr=min(heights[p1],heights[p2])*(p2-p1)
            water=max(water,curr)

            if heights[p1]<heights[p2]:
                p1+=1
            else:
                p2-=1


        return water
            

        