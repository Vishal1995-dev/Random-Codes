class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        a=[]
        for i in range(2):
            if(edges[i][0] in a):
                return edges[i][0]
            else:
                a.append(edges[i][0])
            if(edges[i][1] in a):
                return edges[i][1]
            else:
                a.append(edges[i][1])
