class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent=list(range(n))
        rank=[1]*n

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])

            return parent[x]

        def union(x,y):
            px,py=find(x),find(y)

            if px==py:
                return False
            
            if rank[px]>rank[py]:
                parent[py]=px
            elif rank[py]>rank[px]:
                parent[px]=py

            else:
                parent[py]=px
                rank[px]+=1

            return True


        for u,v in edges:
            if not union(u,v):
                return False


        return True if len({find(i) for i in range(n)})==1 else False
        