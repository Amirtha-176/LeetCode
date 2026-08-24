class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def lca(n1,n2):
            depth_n1=math.floor(log(n1,2))
            depth_n2=math.floor(log(n2,2))
            diff=depth_n2-depth_n1
            if diff<0:
                diff=-diff
                n1,n2=n2,n1
            n2>>=diff
            if n1==n2:
                return n1
            i=0
            while i<n and n1//(2**(i+1))!=n2//(2**(i+1)):
                i+=1
            return lca(n1//2**(i+1),n2//2**(i+1))
        ans=[]
        for i in queries:
            x=lca(i[0],i[1])
            ans.append(math.floor(log(i[0],2))+math.floor(log(i[1],2))-2*math.floor(log(x,2))+1)
        return ans