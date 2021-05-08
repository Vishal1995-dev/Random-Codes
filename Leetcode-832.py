class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        a=[1,0]
        ret=[]
        for i in range(len(image)):
            r=[]
            for j in range(len(image[0])-1,-1,-1):
                r.append(a[image[i][j]])
            ret.append(r)
        return ret
