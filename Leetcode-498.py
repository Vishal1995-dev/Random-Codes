class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if(matrix==[]):
            return []
        a={}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(i+j in a):
                    a[i+j].append(matrix[i][j])
                else:
                    a[i+j]=[matrix[i][j]]
        ret=[]
        i=2
        while(i<=(len(matrix)-1)+(len(matrix[0])-1)):
            a[i]=a[i][::-1]
            i+=2
        for i in range(len(matrix)+len(matrix[0])-1):
            for j in a[i]:
                ret.append(j)
        return ret
