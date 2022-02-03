from collections import defaultdict
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        seen=[]
        graph=defaultdict(list)
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        
        q=[]
        q.append(source)
        while(q):
            val=q.pop(0)
            if(val==destination):
                return True
            if(val not in seen):
                for i in graph[val]:
                    q.append(i)
                seen.append(val)
        return False
