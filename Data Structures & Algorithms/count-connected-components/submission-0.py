class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent=list(range(n))
        rank=[1]*n

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])

            return parent[x]

        def union(x,y):
            px,py=find(x),find(y)

            if px==py:
                return

            if rank[px]>rank[py]:
                parent[py]=px

            elif rank[px]<rank[py]:
                parent[px]=py

            else:
                parent[py]=px
                rank[px]+=1

            return

        for u,v in edges:
            union(u,v)

        return len({find(i) for i in range(n)})

        
        