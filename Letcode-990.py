class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        graph=[[] for i in range(26)]
        
        for i in equations:
            if(i[1]=='='):
                x=ord(i[0])-ord('a')
                y=ord(i[3])-ord('a')
                graph[x].append(y)
                graph[y].append(x)
        
        val=[-1]*26
        t=0
        for i in range(26):
            if[val[i]==-1]:
                t+=1
                stack=[i]
                while(stack):
                    v=stack.pop()
                    for j in graph[v]:
                        if(val[j]==-1):
                            val[j]=t
                            stack.append(j)
        for i in equations:
            if(i[1]=='!'):
                x=ord(i[0])-ord('a')
                y=ord(i[3])-ord('a')
                if x==y:
                    return False
                if(val[x]!=-1 and val[x]==val[y]):
                    return False
        return True
