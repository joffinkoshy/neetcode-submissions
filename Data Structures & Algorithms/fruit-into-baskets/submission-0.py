class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        best=0

        left=0
        seen={}
        

        for right in range(n):
            seen[fruits[right]]=seen.get(fruits[right],0)+1

            while len(seen)>2:
                seen[fruits[left]]-=1
                if seen[fruits[left]]==0:
                    del seen[fruits[left]]
                left+=1


            best=max(best,right-left+1)

        return best


        