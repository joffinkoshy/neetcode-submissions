class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n=len(blocks)
        min_operations=n
        l=0
        count=0

        for r in range(n):
            if blocks[r]=='W':
                count+=1

            while r-l+1>=k:
                min_operations=min(min_operations,count)

                if blocks[l]=="W":
                    count-=1
                    
                l+=1

        return min_operations
            

        